def dataconvert(data):
    """
    converts 12-bytes of data read from the serial port
    into x,y,z,roll,pitch,yaw (inch,inch,inch,deg,deg,deg)
    for a single bird
    """
    xLS, xMS = data[0], data[1]
    yLS, yMS = data[2], data[3]
    zLS, zMS = data[4], data[5]
    yawLS, yawMS = data[6], data[7]
    pitchLS, pitchMS = data[8], data[9]
    rollLS, rollMS = data[10], data[11]
    #
    xLS = ord(xLS) - 128  # change leading bit to zero
    xLS = xLS << 1  # shift bits left
    x = ((xLS + (ord(xMS) * 256)) << 1)
    y = (((ord(yLS) << 1) + (ord(yMS) * 256)) << 1)
    z = (((ord(zLS) << 1) + (ord(zMS) * 256)) << 1)
    yaw = (((ord(yawLS) << 1) + (ord(yawMS) * 256)) << 1)
    pitch = (((ord(pitchLS) << 1) + (ord(pitchMS) * 256)) << 1)
    roll = (((ord(rollLS) << 1) + (ord(rollMS) * 256)) << 1)
    if x > 32767: x -= 65536
    if y > 32767: y -= 65536
    if z > 32767: z -= 65536
    if yaw > 32767: yaw -= 65536
    if pitch > 32767: pitch -= 65536
    if roll > 32767: roll -= 65536
    # convert to inch and deg
    x = x * 144.0 / 32768.0
    y = y * 144.0 / 32768.0
    z = z * 144.0 / 32768.0
    yaw = yaw * 180.0 / 32768.0
    pitch = pitch * 180.0 / 32768.0
    roll = roll * 180.0 / 32768.0
    return x, y, z, roll, pitch, yaw


import serial
import time
import struct

# open the serial port
# ser COM1 is the master ERController
# ser_slave COM4 is the only one slave Bird controller
ser = serial.Serial()
ser.port = "COM1"
ser.baudrate = 115200
ser.open()

ser_slave = serial.Serial()
ser_slave.port = "COM4"
ser_slave.baudrate = 115200
ser_slave.open()

# Hello, bird
print 'Hello to bird'
time.sleep(0.5)
ser.setRTS(True)
time.sleep(0.5)
ser.setRTS(False)

time.sleep(0.5)
ser_slave.setRTS(True)
time.sleep(0.5)
ser_slave.setRTS(False)

# read any junk that might be waiting for us
n = ser.inWaiting()
if n > 0:
    ser.read(n)

n = ser_slave.inWaiting()
if n > 0:
    ser.read(n)
# auto-configure flock

print 'auto-congifuring'
ser.write('P')
ser.write(chr(50))
ser.write(chr(2))

time.sleep(3)

# tell bird we want it to send us 12-byte position/angle data
print 'POS/ANGLE mode'
ser_slave.write('Y')  # send POSITION / ANGLES command
time.sleep(2)

# sampling rate and recording length
fs = 100.0  # Hz
winl = 20.0  # seconds

# loop to record data
t0 = time.time()
tp = time.time()
while time.time() - t0 < winl:
    ti = time.time()
    if ti - tp >= (1.0 / fs):
        tp = time.time()
        ser_slave.write('B')
        while ser_slave.inWaiting() < 12:
            continue
        data = ser_slave.read(12)
        x, y, z, roll, pitch, yaw = dataconvert(data)
        print "%8.3f %8.3f %8.3f %8.3f %8.3f %8.3f %8.3f" % (tp - t0, x, y, z, roll, pitch, yaw)

# goodbye bird
ser.setRTS(True)
ser_slave.setRTS(True)

# close the serial port
ser.close()
ser_slave.close()

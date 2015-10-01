rp1 = 'I:/data/l2r/'
rp2 = 'I:/data/r2l/'

rp = [rp1, rp2]
for j in range(2):
    for i in range(10):
        fn = rp[j] + str(i) + '.csv'
        fn1 = rp[j] + 'u' + str(i) + '.csv'
        with open(fn, 'r') as f:
            with open(fn1, 'w') as f1:
                f.next()
                for line in f:
                    f1.write(line)

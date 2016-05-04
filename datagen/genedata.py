#!/usr/bin/python
import random
from sys import argv

script, baseitems, insertitems, deleteitems, updateitems = argv

baseitems = int(baseitems)
insertitems = int(insertitems)
deleteitems = int(deleteitems)
updateitems = int(updateitems)

base = open('base.txt', 'w+')
for i in xrange(1, baseitems + 1):
    base.write(str(i) + ' aquickbrownfoxjumpsoverthelazydog\n')
base.close()

lines = []

for i in xrange(baseitems + 1, baseitems + insertitems + 1):
    lines.append(str(i) + ' aquickbrownfoxjumpsoverthelazydog 0\n')

for i in xrange(1, deleteitems + 1):
    lines.append(str(i) + ' aquickbrownfoxjumpsoverthelazydog 1\n')

for i in xrange(deleteitems + 1, deleteitems + deleteitems + 1):
    lines.append(str(i) + ' helloworld 2\n')

random.shuffle(lines)

delta = open('delta.txt', 'w+')
for line in lines:
    delta.write(line)
delta.close()

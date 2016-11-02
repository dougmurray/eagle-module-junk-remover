# eagle-module-junk-remover.py
#!usr/bin/env python27
import re
"""Removed unused signals in board XML file that CADSoft Eagle produces
   when modules are imported.

   Author:  Douglass Murray
   Date:  2016-11-01
"""
with open('test-eagle-file.brd', 'r') as f:
    read_data = list(f)
f.closed

print read_data
newestList = []
regex=re.compile(".*(signal).*")
for i, line in enumerate(read_data):
    for m in [regex.search(line)]:
        if m:
            newestList.append([i, m.group(0)])
print newestList

for element in enumerate(newestList):
    for secelement in enumerate(element):
        if secelement == +element:
            print "DELETE"
        else:
            print "NOTHING"

"""
for i, element in enumerate(newestList):
    for n, data in enumerate(newestList):
        if n == +i:
            print "DELETE"
        else:
            print "NOTHING"
"""
"""
newList = [m.group(0) for line in read_data for m in [regex.search(line)] if m]
print newList
"""
"""
for i, data in enumerate(read_data):
        if data=='<signal1>\n':
            print i, 'YES!'
        else:
            print i, 'NO!'
"""

"""Example Operation"""
someList = [10,11,13,15,17,18,20]
n = someList[0]
print n

for i, element in enumerate(someList):
    while element == n:
        if i+1 < len(someList) and someList[i+1] == n+1:
            print "TRUE"
            n = n+1
        else:
            n = n+1
            print "FALSE"
    else:
        n = n+1


# eagle-module-junk-remover.py
#!usr/bin/env python27
import re
"""Removed unused signals in board XML file that CADSoft Eagle produces
   when modules are imported.

   Author:  Douglass Murray
   Date:  2016-11-01
"""

unnecessaryLeader = re.compile('<signal name*')
unnecessaryTail = re.compile('</signal>')

# Import file
inFile = open('file.brd', 'r')
editMe = inFile.readlines()
inFile.close()

locations = []
for i, element in enumerate(editMe):
    if re.match(unnecessaryLeader, element):
        tester = editMe[i+1]
        if re.match(unnecessaryTail, tester):
            locations.append(i)

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


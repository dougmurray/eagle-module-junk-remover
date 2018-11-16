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

for i in sorted(locations, reverse=True):
    del editMe[i]

locations2 = []
for i, element in enumerate(editMe):
    if re.match(unnecessaryTail, element):
        try:
            tester = editMe[i+1]
        except IndexError:
            tester = 'null'
        if re.match(unnecessaryTail, tester):
            locations2.append(i)

for i in sorted(locations2, reverse=True):
    del editMe[i]

# Export to EAGLE board file (xml)
outFile = open('testChanged.brd', 'w')
outFile.writelines(editMe)
outFile.close()

# eagleJunkRemover.py
# Imports an EAGLE board file (xml) and removes extraneous sequential 
# signals that are not actually used, which reduces the file size greatly, 
# allowing faster load times.   
# WARNING: In reality you should use a proper XML parser, 
# but for simple editing like removing sequential xml code
# from an EAGLE board file, this python script will do.
# Author: Doug Murray
# Date: 2018-11-16
import re

# The extra EAGLE board elements are always empty data signal tags
# that begin with <signal name=...> and end with </signal>. 
unnecessaryLeader = re.compile('<signal name*')
unnecessaryTail = re.compile('</signal>')

# Import file
inFile = open('file.brd', 'r')
editMe = inFile.readlines()
inFile.close()

# Find locations of empty signal tags by finding where
# xml <signal name=...> and </signal> tags are consecutive with no
# data between them.
locations = []
for i, element in enumerate(editMe):
    if re.match(unnecessaryLeader, element):
        tester = editMe[i+1]
        if re.match(unnecessaryTail, tester):
            locations.append(i)

# Remove the front of the unnecessary signal tags (<signal name=...>)
for i in sorted(locations, reverse=True):
    del editMe[i]

# Now that all the front empty signals tags are gone
# find the locations of the signal end tags that are now
# consecutively </signal></signal>
locations2 = []
for i, element in enumerate(editMe):
    if re.match(unnecessaryTail, element):
        try:
            tester = editMe[i+1]
        except IndexError:
            tester = 'null'
        if re.match(unnecessaryTail, tester):
            locations2.append(i)

# Remove the end of the unnecessary signal tags that were just found
for i in sorted(locations2, reverse=True):
    del editMe[i]

# After all the deletions there will always be one signal end tag
# not removed due to how for loops work, so remove the last one
del editMe[locations2[0]]

# Export to EAGLE board file (xml)
outFile = open('testChanged.brd', 'w')
outFile.writelines(editMe)
outFile.close()

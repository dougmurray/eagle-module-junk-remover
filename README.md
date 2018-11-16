eagleJunkRemover
=================

Script to remove unnecessary signals that are added to CADSoft EAGLE board files (XML format) when modules are imported.  

**WARNING**: In reality you should use a proper XML parser, but for simple editing like removing sequential xml code from an EAGLE board file, this python script will do.

How to run
-----------

To run the script just type:

	python eagleJunkRemover.py /path/to/file/filename.brd

with the */path/to/file/filename.brd* being the location of the EAGLE file you would like to edit.  

How it works
-------------

When importing an EAGLE design, unused signals are kept in the imported board file which explodes the file size and greatly increases the load time.  These board elements in XML are always empty data signal tags, that begin with *<signal name=...>* and end with *</signal>*.  This python script exploits this pattern and uses regular expressions to systematically remove all these unnecessary XML elements.  
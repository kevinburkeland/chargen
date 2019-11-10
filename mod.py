#!/usr/bin/python
#rev 0.1
#Last modified 11/9/2019
#written by Kevin Burkeland
#converts attributes to mods
def ablemod(attribs):
	amod = {'str':(attribs['str']-10)/2,'dex':(attribs['dex']-10)/2,'con':(attribs['con']-10)/2,'int':(attribs['int']-10)/2,'wis':(attribs['wis']-10)/2,'cha':(attribs['cha']-10)/2}
	return amod

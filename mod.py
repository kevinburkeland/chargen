#!/usr/bin/python
#rev 0.1
#Last modified 11/9/2019
#written by Kevin Burkeland
#converts attributes to mods
import math
def ablemod(attribs):
	amod = {'str':math.floor((attribs['str']-10)/2),'dex':math.floor((attribs['dex']-10)/2),'con':math.floor((attribs['con']-10)/2),'int':math.floor((attribs['int']-10)/2),'wis':math.floor((attribs['wis']-10)/2),'cha':math.floor((attribs['cha']-10)/2)}
	return amod

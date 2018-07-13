#!/usr/bin/python2

import  cgi

print  "Content-type:text/html"
print  ""

data=cgi.FieldStorage()
saas=data.getvalue('s')

if  saas ==  'gedit' :
	print "download source code and run with password  q"
	print  "<a href='http://192.168.10.201/text.sh'>"
	print  "Click here to Download"
	print   "</a>"

elif   saas  ==   "calc":
	print "download source code and run with password  q"
	print  "<a href='http://192.168.10.201/calc.sh'>"
	print  "Click here to Download"
	print   "</a>"



else :
	print  "NO software "

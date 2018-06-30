#!/usr/bin/python

import  cgi,cgitb,commands

print  "Content-Type:text/html"
print  ""

print  "<html>"
print  "<body bgcolor='yellow'>"
print  "<form>"
# checking  running vms
status=commands.getoutput('sudo  virsh list')
for  i  in  status.split():
	if  'adhoc' in i:
		print i+  "<input type='radio' name='oss' value="+i+">"

print  "<input type='submit' value='details'>"
print   "</form>"
print   "</body>"
print  "</html>"


#!/usr/bin/python

import  cgi
import cgitb
cgitb.enable()

print  "Content-Type:text/html"
print  ""

#  storing all the data from client 
client_data=cgi.FieldStorage()
# extracting LANGuage 
web_lang=client_data.getvalue('lang')
print web_lang
#  extracting only OS name 
os_name=client_data.getvalue('os')
print  os_name
#  extracting  only RAM 
os_ram=client_data.getvalue('ram')
print os_ram
#  extracting only CPU in Core 
os_cpu=client_data.getvalue('cpu')
print  os_cpu 



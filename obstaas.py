#!/usr/bin/python2

import cgi,cgitb,commands

cgitb.enable()

print "content-type:text/html"
print  ""

w=cgi.FieldStorage()

st_name=w.getvalue('name')
st_size=w.getvalue('size')

# Now creating  

print  commands.getoutput('sudo lvcreate --name  '+st_name+'  --size '+st_size+'M openvg')
#  format  
print  commands.getoutput('sudo mkfs.xfs   /dev/openvg/'+st_name)

#  creating account  
#  
print  commands.getoutput('sudo  mkdir  /var/www/html/'+st_name)
print  commands.getoutput('sudo  mount /dev/openvg/'+st_name+'  /var/www/html/'+st_name)




# Python 2.6.6
# Sonar 4.5.1
# script to list sonar projects which are inactive more than x days and delete them. 

import json
import urllib
import time
import datetime
import urllib2


def delete_sonar_project(id, key, name):
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request('http://sonarqube/api/projects/' + key)
	request.add_header( 'Authorization', b'Basic ' + 'username:pwd'.encode('base64').replace('\n','') )
	request.get_method = lambda: 'DELETE'
	url = opener.open(request)
	print "The sonar project ", id, key, name," is deleted" 
	return;

No = 868
url = 'http://sonarqube/api/resources'

r = urllib.urlopen(url)
data = json.loads(r.read().decode("utf-8"))
today = datetime.date.today()

for data1 in data:
	x = data1["date"]
	#days_between(x, 2016-08-18)
	y = int(x[:4])
	m = int(x[5:7])
	d = int(x[8:10])
	#print x[:10] + y + m + d
	dateof = datetime.date(y, m, d)
	delta = dateof - today
	
	daysno = str(-delta.days)
	#print today, dateof, y, m, d, daysno
	i = 1
	#print "Date :", x[:10], "No. of days ", daysno[:2]
	try:
		if (int(daysno) > No):
			print data1["id"], data1["key"], data1["name"], daysno
			delete_sonar_project(data1["id"], data1["key"], data1["name"]);	
	except Exception, e:
			print "Throwing exception", data1["id"], data1["key"]

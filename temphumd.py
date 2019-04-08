#!/usr/bin/python
import Adafruit_DHT as dht
from datetime import datetime
humidity, temperature = dht.read_retry(dht.AM2302, 4)
temperature = temperature * 9/5.0 + 32
localtime = datetime.now()
if humidity is not None and temperature is not None:
    output = '{{ "index" : "MasterBedroom-{0}", "datetime" : "{0}", "location" : "MasterBedroom", "Temp" : "{1:0.1f}", "Humidity" : "{2:0.1f}%" }}'.format(localtime, temperature, humidity)
else:
    output = 'Failed to get reading. Try again!'
fh = open("/home/svcnodered/output.txt", "a")
fh.write(output)
fh.close()
#This is a test.  Update worked successfully!
#Testing clone again.  chmod +x might need to be done for each pull
#Another change

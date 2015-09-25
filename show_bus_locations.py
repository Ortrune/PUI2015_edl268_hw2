import json
import sys
import urllib2

# open data from inputted URL
url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
request = urllib2.urlopen(url)
data = json.loads(request.read())

# acquire bus line, set 'buses' reference, set count of buses
busLine = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']
buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
busCount = 0

print 'Bus Line : %s' % (busLine)

# count and print total number of buses
for bus in buses:
	for i in bus['VehicleActivity']:
		busCount = busCount + 1
		
print 'Number of Active Buses : %s' % (busCount)

# acquire and print bus number, latitude, and longitude
for bus in buses:
	busCount = 0
	for i in bus['VehicleActivity']:
		busLat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		busLong = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print 'Bus %s is at latitude %s and longitude %s' % (busCount, busLat, busLong)
		busCount = busCount + 1 
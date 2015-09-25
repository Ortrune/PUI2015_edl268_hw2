import json
import sys
import urllib2
import csv

# open data from inputted URL
url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
request = urllib2.urlopen(url)
data = json.loads(request.read())

# set 'buses' reference
buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']

# create csv file and write headers
with open(sys.argv[3], 'wb') as csvFile:
	writer = csv.writer(csvFile)
	headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
	writer.writerow(headers)

# acquire latitude, longitude, and OnwardCall information if it is available
# write acquired data to csv file
	for bus in buses:
		for i in bus['VehicleActivity']:
			busLat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			busLong = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
			if 'OnwardCall' not in i['MonitoredVehicleJourney']['OnwardCalls']:
				busStop = 'N/A'
				busDist = 'N/A'
			else:
				busStop = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
				busDist = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
				
			writer.writerow([busLat, busLong, busStop, busDist])
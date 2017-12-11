import json
import urllib2
from pprint import pprint

AdotJfile = 'http://172.20.221.179/dump1090/data/aircraft.json'

data = json.load(urllib2.urlopen(AdotJfile))

filtered = {}

for ac in data['aircraft']:
    try:
        filtered[ac['hex']] = { 'position' : [ ac['lat'], ac['lon'], ac['altitude'] ], 
                            'vector' : [ ac['track'], ac['vert_rate'], ac['speed'] ],
                            'time' : data['now'] - ac['seen']}
    except KeyError:
        pass

pprint(filtered, indent=1)
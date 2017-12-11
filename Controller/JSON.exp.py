import json
import urllib2
from pprint import pprint

AdotJfile = 'http://172.20.221.179/dump1090/data/aircraft.json'

data = json.load(urllib2.urlopen(AdotJfile))

pprint(data, indent=1)
# coding: utf-8

import re

from pprint import pprint


with open('station_name.html', 'r') as f:
	text = f.read()
	stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-z]+)', text)
	pprint(dict(stations), indent=4)

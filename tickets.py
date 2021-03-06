# coding: utf-8

"""Train tickets query via command-line.

Usage:
	tickets [-gdtkz] <from> <to> <date>

Options:
	-h,--help	display the help menu
	-g		高铁
	-d		动车
	-t		特快
	-k		快速
	-z		直达

Example:
	tickets 南京 北京 2016-07-01
	tickets -dg 南京 北京 2016-07-01
"""

from docopt import docopt
from stations import stations
import requests
from prettytable import PrettyTable

def cli():
	"""command-line interface"""
	arguments = docopt(__doc__)
#	print(arguments)
	from_station = stations.get(arguments['<from>'])
	to_station = stations.get(arguments['<to>'])
	date = arguments['<date>']
	# build the URL
	url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date, from_station, to_station)
	
	# add 'verify=False' parameter, do not verify the certificate.
	r = requests.get(url, verify=False)
	rows = r.json()['data']['datas']
#	print(rows)
	headers = '车次 车站 时间 历时 商务 一等 二等 软卧 硬卧 软座 硬座 无座'.split()
	pt = PrettyTable()
	pt._set_field_names(headers)
	for row in rows:
	#  pt.add_row()
	#	iooo = 1	
		row_table = [ 
			# 车次
			row.get('station_train_code'),
			# 车站
			'\n'.join([ row.get('from_station_name'), row.get('to_station_name')]),
			# 时间
			'\n'.join([ row.get('start_time'), row.get('arrive_time')]),
			# 历时
			row.get('lishi'),
			# 商务
			row.get('swz_num'),
			# 一等
			row.get('zy_num'),
			# 二等
			row.get('ze_num'),
			# 软卧
			row.get('rw_num'),
			# 硬卧
			row.get('yw_num'),
			# 软座
			row.get('rz_num'),
			# 硬座
			row.get('yz_num'),
			# 无座
			row.get('wz_num')
		]
		pt.add_row(row_table)
	print(pt)

if __name__ == '__main__':
	cli()

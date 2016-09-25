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


def cli():
	"""command-line interface"""
	arguments = docopt(__doc__)
	print(arguments)


if __name__ == '__main__':
	cli()

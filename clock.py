from time import gmtime, strftime
from microbit import *

while True:
	now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	date, time = now.split()
	h, m, s = time.split(':')
	display.show(h + ' :')
	display.show(m + ' :')
	display.show(s)


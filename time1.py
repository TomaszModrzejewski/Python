import time

def time_struct(s):
	   print(' tm_year :', s.tm_year)
	   print(' tm_mon :', s.tm_mon)
	   print(' tm_mday :', s.tm_mday)
	   print(' tm_hour :', s.tm_hour)
	   print(' tm_min :', s.tm_min)
	   print(' tm_sec :', s.tm_sec)
	   print(' tm_wday :', s.tm_wday)
	   print(' tm_yday :', s.tm_yday)
	   print(' tm_isdst:', s.tm_isdst)
print('\nlocaltime:')
time_struct(time.localtime())
print('\ngmtime:')
time_struct(time.gmtime())

	
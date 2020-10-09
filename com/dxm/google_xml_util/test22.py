# encoding:utf-8
import sys

import pytz
import datetime

tz = pytz.timezone('UTC')
now = datetime.datetime.now(tz)
str_now = now.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
print '{}_1'.format('中国')
reload(sys)
print sys.setdefaultencoding("utf-8")
for zone in pytz.all_timezones:
    now = datetime.datetime.now(pytz.timezone(zone))
    print zone,now.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
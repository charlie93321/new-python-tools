from datetime import datetime, timezone, timedelta
# 创建时区UTC+00:00
tz_utc = timezone(timedelta(hours=0))
# 获得带时区的UTC时间
current_time_utc = datetime.utcnow().replace(tzinfo=tz_utc,microsecond=0)
timestr = current_time_utc.strftime("%Y-%m-%dT%H:%M:%S%z")
new_time_str="{}:{}".format(timestr[0:-2],timestr[-2:])
print(new_time_str)

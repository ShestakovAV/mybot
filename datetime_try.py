from datetime import datetime
from datetime import timedelta
local_time = datetime.now()
print(local_time)
tomorrow = local_time + timedelta(days = 1)
yesterday = local_time - timedelta(days = 1)
farawey_time = local_time + 30*timedelta(days = 1)
print(tomorrow.strftime('%d.%m.%Y %H:%M'))
print(yesterday.strftime('%d.%m.%Y %H:%M'))
print(farawey_time.strftime('%d.%m.%Y %H:%M'))

date_string = "01/01/25 12:10:03.234567"
dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
print(dt)
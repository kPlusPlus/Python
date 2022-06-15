from datetime import datetime

date_time_str = '18/09/19 01:55:19'
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)


dt_str = '2022-05-12 20:34:00'
from dateutil import parser
dt_obj = parser.parse(dt_str)

print("The type of the date is now",  type(dt_obj))
print("The date is", dt_obj)
#pip instal pytz
import datetime
import pytz

data = datetime.datetime.now(pytz.timezone('Europe/Oslo'))
print(data)
'''
O módulo 'datetime' é usado para lidar com datas e horas. Ele possui várias classes úteis como date, time e timedelta.

aware - carrega informação de fuso horário
naive - não carrega informação de fuso horário (UTC)

'''
from datetime import date, datetime, time

#objeto date
print('date object')
data = date(2025, 1, 1)

print(data)
print(date.today())

#objeto datetime
print('datetime object')
data_hour = datetime(2025, 1, 1, 18, 30, 2)
print(data_hour)
data_today = datetime.today()
print(data_today)

#time object
print('time object')
hour = time(18, 30, 2)
print(hour)
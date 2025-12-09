'''
O objeto timedelta representa uma duração, a diferença entre duas instâncias datetime ou date. Não trabalho só com o objeto time.

class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
'''

from datetime import timedelta, datetime

data_hour = datetime(2025, 1, 1, 18, 30, 2)
print(data_hour)

add_week = data_hour + timedelta(days=3)

print(add_week)

#Contornando o problema de operar em horas
result = datetime.now() + timedelta(hours=2)
print(result.time())
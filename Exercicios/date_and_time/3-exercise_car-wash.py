'''
Simular um sistema de lava - jato que tem como parâmetro de entrada o tipo de carro.
O sistema deve informar o tempo de realização do serviço.
'''

from datetime import datetime, timedelta

car_type = int(input(f'''
          Bem-vindo ao lava a jato flash
          Por favor, informe o tipo de carro:
          1 - compacto
          2 - médio
          3 - grande 
          Entre com o valor -> '''))

service_time_small = 30
service_time_medium = 45
service_time_big = 60

current_time = datetime.now()
final_time = 0

if car_type == 1:
    final_time = current_time + timedelta(minutes = service_time_small)
elif car_type == 2:
    final_time = current_time + timedelta(minutes = service_time_medium)
else:
    final_time = current_time + timedelta(minutes = service_time_big)

print(f'''
Hora de chegada: {current_time}
Hora de saída: {final_time}
''')
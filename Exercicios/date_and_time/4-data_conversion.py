'''
strftime = Converte objeto para uma string conforme um formato fornecido
strptime = Interpreta uma string como um objeto dado um formato correspondente

'''
from datetime import datetime

# Formatando a data
current_data = datetime.now()
mask_ptBR = '%d/%m/%Y %a'
print(current_data.strftime(mask_ptBR))

#Conversão de string para datetime
data_string = "02/01/2025 10:30"
mask_eng = '%d/%m/%Y %H:%M'
print(datetime.strptime(data_string, mask_eng))
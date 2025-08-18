from datetime import date, datetime, time

data = date(2023, 7, 10) # apenas coloca no formato 
print(data)
print(date.today()) # importa data atual pelo sistema

data_hora = datetime(2023, 7, 10, 20, 30, 20)
print(data_hora) # formato date e hora
print(datetime.today()) # data e hora importada do sistema

hora = time(10, 20, 0)
print(hora)
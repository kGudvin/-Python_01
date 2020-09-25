a = int(input('Введите время в секундах: '))
hours = a // 3600
minutes = (a % 3600) // 60
seconds = a % 60
print('{} : {} : {}'.format(hours, minutes, seconds))
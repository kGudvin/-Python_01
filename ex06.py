first_result = int(input('Введите результат первого дня: '))
final_result = int(input('Введите конечный результат: '))
counter = 1
while first_result < final_result:
    first_result *= 1.1
    counter += 1
print(counter)
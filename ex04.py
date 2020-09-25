number = int(input('Введите целое положительное число: '))

last_digit = number % 10
number //= 10
while number > 0:
    if number % 10 > last_digit:
        last_digit = number % 10
    number //= 10
print(last_digit)
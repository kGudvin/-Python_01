profit = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))

if profit > costs:
    print('Фирма отработала с прибылью')
    profitability_of_proceeds = profit - costs
    print('Рентабельность фирмы: ', profitability_of_proceeds / profit)
    number_of_employees = int(input('Введите численность сотрудников '))
    print('Прибыль в расчете на одного сотрудника составляет ', profitability_of_proceeds / number_of_employees)
elif profit == costs:
    print('Фирма отработала в ноль')
else:
    print('Фирма отработала с убытком')

first = int(input('Введите первое число и нажмите Enter '))
second = int(input('Введите второе число и нажмите Enter '))
third = int(input('Введите третье число и нажмите Enter '))
if first == second == third:
    print(3)
elif first == second != third or first != second == third or first == third != second:
    print(2)
else:
    print(0)
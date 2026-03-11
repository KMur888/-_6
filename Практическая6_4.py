def schastliviy_bilet(nomer):
    dlina = len(nomer)
    polovina = dlina // 2
    
    # Сумма первой половины
    summa1 = 0
    for i in range(polovina):
        summa1 = summa1 + int(nomer[i])
    
    # Сумма второй половины
    summa2 = 0
    for i in range(polovina, dlina):
        summa2 = summa2 + int(nomer[i])
    
    # Сравниваем суммы
    if summa1 == summa2:
        return True
    else:
        return False

# Основная программа
nomer = input("Введите номер билета (четное количество цифр): ")

# Проверяем, что количество цифр четное
if len(nomer) % 2 != 0:
    print("Ошибка! Количество цифр должно быть четным")
else:
    if schastliviy_bilet(nomer):
        print("Счастливый билет!")
    else:
        print("Обычный билет")
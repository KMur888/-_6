def magicheskaya_data(data):
    den = int(data[0:2])        # первые 2 символа - день
    mesyac = int(data[3:5])      # символы с 3 по 5 - месяц
    god = int(data[6:10])         # символы с 6 по 10 - год
    
    # Берем последние две цифры года
    poslednie_dve = god % 100
    
    # Проверяем условие: день * месяц = последние две цифры года
    if den * mesyac == poslednie_dve:
        return True
    else:
        return False

# Основная программа
data = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if magicheskaya_data(data):
    print("Это магическая дата!")
else:
    print("Это обычная дата")
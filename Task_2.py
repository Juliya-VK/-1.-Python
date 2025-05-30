"""Задача 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

while True:
    # Запрашиваем ввод числа
    num = input("Введите число от 0 до 100000: ")
    
    # Проверяем, что введено целое число
    if not num.isdigit():
        print("Ошибка! Введите целое число.")
        continue
    
    num = int(num)
    
    # Проверяем диапазон числа
    if num < 0 or num > 100000:
        print("Число должно быть от 0 до 100000!")
        continue
    
    break  # Если всё правильно, выходим из цикла

# Проверяем особые случаи
if num <= 1:
    print(f"{num} — не простое и не составное (натуральные числа > 1).")
else:
    # Предполагаем, что число простое, пока не найдём делитель
    is_prime = True
    
    # Проверяем делители от 2 до квадратного корня из числа
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            is_prime = False
            break
    
    # Выводим результат
    if is_prime:
        print(f"{num} — простое число.")
    else:
        print(f"{num} — составное число.")

     
"""Задача 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
 Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
 Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)"""

from random import randint

# Задаём границы
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10

# Генерируем случайное число
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

print(f"Угадай число от {LOWER_LIMIT} до {UPPER_LIMIT}. У тебя {ATTEMPTS} попыток!")

# Основной цикл игры
for attempt in range(1, ATTEMPTS + 1):
    # Получаем предположение игрока
    guess = int(input(f"Попытка {attempt}. Твой вариант: "))
    
    # Проверяем угадал ли
    if guess == secret_number:
        print(f"Поздравляю! Ты угадал число {secret_number} за {attempt} попыток!")
        break
    elif guess < secret_number:
        print("Загаданное число БОЛЬШЕ")
    else:
        print("Загаданное число МЕНЬШЕ")
else:
    # Этот блок выполнится, если цикл не был прерван break
    print(f"К сожалению, попытки закончились. Загаданное число было {secret_number}")
    
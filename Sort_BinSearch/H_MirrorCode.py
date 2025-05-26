from collections import Counter

# Ввод данных
n = int(input().strip())
s = input().strip()

# Подсчет частот букв
freq = Counter(s)

# Формируем левую часть палиндрома и выбираем центральную букву
left_part = []
middle = ""

# Перебираем буквы в алфавитном порядке
for char in sorted(freq.keys()):
    count = freq[char]
    if count % 2 == 1:  # Если количество нечетное, выбираем первую возможную букву в центр
        if middle == "":
            middle = char
        count -= 1  # Убираем одну букву, чтобы сделать четным

    left_part.append(char * (count // 2))  # Добавляем половину оставшихся букв в левую часть

# Формируем палиндром
left_part = "".join(left_part)
palindrome = left_part + middle + left_part[::-1]

# Выводим результат
print(palindrome)

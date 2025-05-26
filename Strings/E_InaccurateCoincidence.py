def find_approximate_matches(p, t):
    len_p = len(p)
    len_t = len(t)
    
    # Список для хранения индексов вхождений
    matches = []
    
    # Пробегаем по строке t с шагом по длине p
    for i in range(len_t - len_p + 1):
        # Вычисляем количество несовпадений
        mismatches = 0
        for j in range(len_p):
            if p[j] != t[i + j]:
                mismatches += 1
                if mismatches > 1:  # Если несовпадений больше одного, выходим из цикла
                    break
        if mismatches <= 1:
            matches.append(i + 1)  # Индексы начинаются с 1, поэтому добавляем 1
    
    return matches

def main():
    # Читаем входные данные
    p = input().strip()  # Подстрока
    t = input().strip()  # Текст
    
    # Получаем все вхождения с точностью до одного несовпадения
    matches = find_approximate_matches(p, t)
    
    # Выводим результат
    print(len(matches))
    if matches:
        print(" ".join(map(str, matches)))

if __name__ == "__main__":
    main()

def compute_prefix_function(pattern):
    """Строит префикс-функцию для строки pattern."""
    m = len(pattern)
    prefix_function = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_function[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_function[i] = j
    return prefix_function

def find_all_occurrences(text, pattern):
    """Возвращает список всех индексов, где встречается pattern в text с использованием алгоритма KMP."""
    n = len(text)
    m = len(pattern)
    if m > n:
        return []  # Если подстрока длиннее строки, нет вхождений
    
    prefix_function = compute_prefix_function(pattern)
    positions = []
    j = 0  # Индекс для подстроки pattern
    
    for i in range(n):  # Проходим по строке text
        while j > 0 and text[i] != pattern[j]:
            j = prefix_function[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == m:
            positions.append(i - m + 1)  # Найдено вхождение, сохраняем индекс начала
            j = prefix_function[j - 1]  # Продолжаем искать дальше
    
    return positions

def main():
    # Читаем входные данные
    T = input().strip()  # Основная строка
    if not T:
        return  # Если строка пустая, выходим

    q = int(input().strip())  # Количество запросов
    if q == 0:
        return  # Если запросов нет, выходим

    queries = [input().strip() for _ in range(q)]  # Все запросы

    # Обрабатываем каждый запрос
    for query in queries:
        if not query:
            print(0)  # Если запрос пустой, выводим 0
            continue
        positions = find_all_occurrences(T, query)
        # Выводим количество вхождений и сами позиции
        print(len(positions), *positions if positions else '')

if __name__ == "__main__":
    main()

def damerau_levenshtein(s, t):
    # Добавляем «пустой» символ в начало, чтобы перейти к 1-based индексам
    s = ' ' + s
    t = ' ' + t
    len_s = len(s) - 1
    len_t = len(t) - 1

    # da[c] будет хранить последнюю строку i, в которой встретился символ c (A..Z)
    da = [0] * 26

    # «Бесконечная» дистанция для границ
    maxdist = len_s + len_t

    # Создаём матрицу размера (len_s+2) x (len_t+2)
    d = [[0] * (len_t + 2) for _ in range(len_s + 2)]

    # Инициализация «границ» (крайних строк и столбцов)
    d[0][0] = maxdist
    for i in range(len_s + 1):
        d[i+1][0] = maxdist
        d[i+1][1] = i
    for j in range(len_t + 1):
        d[0][j+1] = maxdist
        d[1][j+1] = j

    # Основной цикл:
    # i пробегает 1..len_s, j пробегает 1..len_t
    for i in range(1, len_s + 1):
        # db = последняя позиция j, где s[i] == t[j]
        db = 0
        for j in range(1, len_t + 1):
            # i1 = строка, где в s ранее встречался t[j]
            i1 = da[ord(t[j]) - ord('A')]
            # j1 = столбец, где в t ранее встречался s[i]
            j1 = db

            if s[i] == t[j]:
                cost = 0
                db = j
            else:
                cost = 1

            # 1) замена/совпадение
            substitution = d[i][j] + cost
            # 2) вставка символа t[j] в s
            insertion = d[i+1][j] + 1
            # 3) удаление символа s[i]
            deletion = d[i][j+1] + 1
            # 4) перестановка соседних символов
            transpose = d[i1][j1] + (i - i1 - 1) + 1 + (j - j1 - 1)

            d[i+1][j+1] = min(substitution, insertion, deletion, transpose)

        # После обработки всей строки i, запоминаем, что последний раз s[i] встречается в строке i
        da[ord(s[i]) - ord('A')] = i

    return d[len_s+1][len_t+1]


def main():
    s = input().strip()
    t = input().strip()
    print(damerau_levenshtein(s, t))


if __name__ == "__main__":
    main()

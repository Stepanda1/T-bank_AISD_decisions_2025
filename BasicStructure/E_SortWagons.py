def sort_train():
    N = int(input())  # Количество вагонов
    train = list(map(int, input().split()))  # Исходный порядок вагонов
    
    stack = []
    expected = 1  # Ожидаемый номер вагона, который нужно вывести
    actions = []
    
    i = 0
    while i < N:
        count = 0
        while i < N:  # Завозим в тупик подряд идущие вагоны
            stack.append(train[i])
            count += 1
            i += 1
            if i == N or train[i] > train[i - 1]:  # Останавливаемся, если больше завозить нельзя
                break
        actions.append((1, count))  # Запоминаем завоз в тупик
        
        count = 0
        while stack and stack[-1] == expected:  # Выгружаем вагоны в правильном порядке
            stack.pop()
            expected += 1
            count += 1

        if count:
            actions.append((2, count))  # Запоминаем выгрузку

    if stack:  # Если остались вагоны, значит, нельзя отсортировать
        print(0)
    else:
        print(len(actions))
        for action in actions:
            print(*action)

sort_train()


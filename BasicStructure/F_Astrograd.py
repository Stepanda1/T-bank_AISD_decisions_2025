import sys
from collections import deque

def process_events():
    n = int(sys.stdin.readline())  # Количество событий
    queue = deque()  # Очередь
    index_map = {}  # Словарь {id: индекс в очереди}
    output = []  # Ответы на запросы типа 4 и 5

    for _ in range(n):
        event = sys.stdin.readline().split()
        event_type = int(event[0])

        if event_type == 1:  # Добавление человека
            person_id = int(event[1])
            queue.append(person_id)
            index_map[person_id] = len(queue) - 1  # Запоминаем индекс в очереди

        elif event_type == 2:  # Уход первого человека
            if queue:
                left_person = queue.popleft()
                del index_map[left_person]  # Удаляем из словаря
                # Смещаем индексы всех оставшихся
                for key in index_map:
                    index_map[key] -= 1

        elif event_type == 3:  # Уход последнего человека
            if queue:
                right_person = queue.pop()
                del index_map[right_person]  # Удаляем из словаря

        elif event_type == 4:  # Сколько перед q?
            query_id = int(event[1])
            if query_id in index_map:
                output.append(str(index_map[query_id]))
            else:
                output.append("0")  # Если человека нет в очереди

        elif event_type == 5:  # Кто первый в очереди?
            if queue:
                output.append(str(queue[0]))
            else:
                output.append("0")  # Очередь пуста

    sys.stdout.write("\n".join(output) + "\n")  # Оптимизированный вывод

process_events()


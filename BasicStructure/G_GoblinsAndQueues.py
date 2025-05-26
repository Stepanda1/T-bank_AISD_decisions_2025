import sys
from collections import deque

def goblin_queue():
    n = int(sys.stdin.readline().strip())  # Количество запросов
    left_queue = deque()  # Левая половина (центральная часть)
    right_queue = deque()  # Правая половина (обычная очередь)
    
    output = []  # Для хранения вывода

    for _ in range(n):
        command = sys.stdin.readline().split()
        
        if command[0] == '+':  # Обычный гоблин (в конец)
            right_queue.append(command[1])

        elif command[0] == '*':  # Привилегированный гоблин (в середину)
            left_queue.append(command[1])
        
        elif command[0] == '-':  # Уход первого гоблина
            if left_queue:
                output.append(left_queue.popleft())
            else:
                output.append(right_queue.popleft())

        # Балансировка: левая очередь должна быть не короче правой
        if len(left_queue) < len(right_queue):
            left_queue.append(right_queue.popleft())
        elif len(left_queue) > len(right_queue) + 1:
            right_queue.appendleft(left_queue.pop())

    sys.stdout.write("\n".join(output) + "\n")  # Быстрый вывод

goblin_queue()


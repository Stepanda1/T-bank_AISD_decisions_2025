import sys

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        # Добавляем элемент в конец
        self.heap.append(x)
        # Восстанавливаем кучу с помощью heapify-up
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        # Извлекаем максимальный элемент (корень)
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        # Перемещаем последний элемент в корень
        self.heap[0] = self.heap.pop()
        # Восстанавливаем кучу с помощью heapify-down
        self._heapify_down(0)
        
        return root

    def _heapify_up(self, idx):
        # Поднимаем элемент вверх, чтобы восстановить свойство кучи
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _heapify_down(self, idx):
        # Опускаем элемент вниз, чтобы восстановить свойство кучи
        n = len(self.heap)
        while 2 * idx + 1 < n:  # Пока есть хотя бы один левый ребенок
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            # Находим наибольшего из родителей и двух детей
            if self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            # Если наибольший элемент не родитель, меняем их местами
            if largest != idx:
                self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                idx = largest
            else:
                break

def solve():
    n = int(input())  # Читаем количество команд
    max_heap = MaxHeap()  # Создаем экземпляр максимальной кучи
    results = []

    for _ in range(n):
        command = input().split()
        
        if command[0] == '0':
            # Операция Insert(X)
            max_heap.insert(int(command[1]))
        elif command[0] == '1':
            # Операция Extract
            results.append(str(max_heap.extract()))
    
    # Выводим все результаты для операции Extract
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

import sys

class MaxHeap:
    def __init__(self, arr):
        self.heap = arr
        self.n = len(arr)
        # Строим кучу
        self._build_heap()

    def _heapify_down(self, idx):
        # Опускаем элемент вниз по дереву, восстанавливая свойство кучи
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        
        if left < self.n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.n and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._heapify_down(largest)

    def _heapify_up(self, idx):
        # Поднимаем элемент вверх по дереву
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _build_heap(self):
        # Строим кучу с конца (от последнего узла) до корня
        for i in range(self.n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def extract_max(self):
        if self.n <= 0:
            return None
        root = self.heap[0]
        # Перемещаем последний элемент на место корня
        self.heap[0] = self.heap[self.n - 1]
        self.n -= 1
        self._heapify_down(0)
        return root

    def add(self, value):
        # Добавляем новый элемент в кучу
        self.heap.append(value)
        self.n += 1
        self._heapify_up(self.n - 1)

def solve():
    n = int(input())  # Читаем количество элементов
    arr = list(map(int, input().split()))  # Читаем массив
    
    # Строим кучу
    heap = MaxHeap(arr)
    
    # Сортируем массив с помощью кучи
    sorted_arr = []
    while heap.n > 0:
        sorted_arr.append(heap.extract_max())
    
    # Инвертируем отсортированный массив для вывода в обратном порядке
    sorted_arr.reverse()
    
    # Выводим отсортированный массив в обратном порядке
    print(" ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    solve()

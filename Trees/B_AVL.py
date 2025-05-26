import sys

# Чтение данных
sys.setrecursionlimit(200000)

def check_avl(v, tree, values, depth=0):
    if v == -1:
        return True, 0  # Пустое поддерево, считается сбалансированным с высотой 0

    left, right = tree[v]  # Получаем левое и правое поддерево
    left_is_avl, left_height = check_avl(left, tree, values, depth + 1)
    right_is_avl, right_height = check_avl(right, tree, values, depth + 1)

    if not left_is_avl or not right_is_avl:
        return False, 0  # Если хотя бы одно поддерево не является AVL, сразу возвращаем False

    if abs(left_height - right_height) > 1:
        return False, 0  # Если разница в высотах поддеревьев больше 1, дерево не AVL

    # Проверяем корректность значений в поддеревьях
    if left != -1 and values[left] >= values[v]:  # Левый потомок должен быть меньше текущего
        return False, 0
    if right != -1 and values[right] <= values[v]:  # Правый потомок должен быть больше текущего
        return False, 0

    # Возвращаем True и высоту текущего поддерева
    return True, max(left_height, right_height) + 1

def is_avl(n, r, tree, values):
    is_avl_tree, _ = check_avl(r, tree, values)
    return 1 if is_avl_tree else 0

if __name__ == "__main__":
    n, r = map(int, input().split())  # количество вершин и корень
    tree = []
    values = [0] * n

    # Чтение структуры дерева
    for i in range(n):
        li, ri = map(int, input().split())
        tree.append((li, ri))  # Для каждой вершины храним левого и правого ребенка
        values[i] = i  # Значение вершины i - это i, т.к. вершины индексированы от 0 до n-1

    # Проверка, является ли дерево AVL
    print(is_avl(n, r, tree, values))


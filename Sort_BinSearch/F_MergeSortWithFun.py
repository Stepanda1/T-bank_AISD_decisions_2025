def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Начальный индекс для левого подмассива
    j = mid + 1 # Начальный индекс для правого подмассива
    k = left    # Начальный индекс для слияния
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # Есть инверсии: все элементы от i до mid инверсированы с arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Копируем оставшиеся элементы левого подмассива
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы правого подмассива
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Копируем отсортированные элементы обратно в оригинальный массив
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

# Ввод данных
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Временный массив
temp_arr = [0] * n

# Подсчет инверсий и сортировка
inv_count = merge_sort_and_count(arr, temp_arr, 0, n - 1)

# Вывод результатов
print(inv_count)
print(' '.join(map(str, arr)))

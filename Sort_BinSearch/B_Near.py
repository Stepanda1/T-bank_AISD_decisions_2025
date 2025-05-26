def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
nums = list(map(int,input().split()))
n = nums[0]
k = nums[1]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(len(b)):
    if binary_search(a,b[i])!=-1:
        print(b[i])
    else:
        c = 2*10**9
        for j in range(len(a)):
            if abs(a[j]-b[i]) < c:
                c = abs(a[j]-b[i])
                result = a[j]
            elif abs(a[j]-b[i]) == c:
                t = 1
        print(result)
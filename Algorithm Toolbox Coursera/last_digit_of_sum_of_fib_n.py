def fibonacci(n):
    arr = list(range(n + 1))
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    result = arr[n]
    return int(str(result)[-1])


n = int(input())
print(fibonacci(n))

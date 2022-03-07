def fibonacci(n):
    arr = list(range(n + 1))
    # print(arr)
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


n = int(input())

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(n))
# print(fibonacci(n))

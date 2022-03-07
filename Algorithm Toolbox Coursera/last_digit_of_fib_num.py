def fib_num(f, n):
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10
    return f


def last_digit_of_fibonacci(n):
    f = [0] * 61
    f = fib_num(f, 60)
    return f[n % 60]


n = int(input())
print(last_digit_of_fibonacci(n))

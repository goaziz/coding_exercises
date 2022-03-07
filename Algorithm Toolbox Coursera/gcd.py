a, b = [int(i) for i in input().split()]


def gcd(a, b):
    if b == 0:
        return a

    rem = a % b
    return gcd(b, rem)


print(gcd(a, b))

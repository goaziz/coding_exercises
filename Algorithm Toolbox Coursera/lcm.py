def gcd(a, b):
    if b == 0:
        return a

    rem = a % b
    return gcd(b, rem)


def lcm(a, b):
    if b == 0:
        return a
    else:
        division = gcd(a, b)
        return (a * b) // division


a, b = [int(i) for i in input().split()]
print(lcm(a, b))

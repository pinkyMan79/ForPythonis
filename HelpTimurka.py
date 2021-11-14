from random import randint


# 2
def f(a, b):
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                return i


a = [1, 2, 3]
b = [2, 3, 4]

print(f(a, b))


# 4
def buble(a):
    t = 0
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j + 1]:
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t
    return a


c = []

for i in range(0, 10):
    c.append(randint(0, 10))

print(buble(c))

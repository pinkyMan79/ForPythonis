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

# HW #3

# 1

import os


def checkForFile(fileName, f):
    for element in os.scandir(f):
        if element.is_file():
            if element.name == fileName:
                yield f
        else:
            yield from checkForFile(fileName, element.path)


fName = (str(input())) + ''
print(*checkForFile(fName, os.getcwd()))

# 2 Console

import shutil

path = ''


def ls(dir):
    print(os.listdir(path="" + dir))


def cd(way):
    os.chdir(way)


def copy(n1, n2):
    shutil.copyfile(n1, n2)


while (True):
    inp = input() + ''
    if inp == "ls":
        ls(os.getcwd())
    elif inp == "cd":
        print("input directory u want to go")
        i = input()
        cd(i)
        print("succes")
    elif inp == "copy":
        print("from")
        i = input()
        print("to")
        i1 = input()
        copy(i, i1)
    elif inp == "exit":
        print("bye")
        break

# 3 Cjntrol work

# 2

n = int(input())

a = []

for i in range(n):
    ad = int(input())
    a.append(ad)

for i in range(0, n // 2):
    t = a[i]
    a[i] = a[n - i - 1]
    a[n - i - 1] = t

print(a)

# 3

n = int(input())

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(int(input()))

mat2 = matrix

for i in range(n):
    for j in range(n):
        mat2[i][j] = (matrix[i][j - 1] + matrix[i][j])

for i in range(n):
    print(mat2[i])


# 1

def sov(n):
    a = []
    sum = 0
    for i in range(n):
        if n % i == 0 and i > 0:
            a.append(i)
    for i in a:
        sum += i
    if sum == n:
        return True
    else:
        return False


for i in range(1, 5001):
    if sov(i):
        print(i)

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


fName = (str(input()) + '.py') + ''
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

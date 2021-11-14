a = [0] * 217
for i in range(len(a)):
    if i * 3 >= 51:
        a[i] = 1

for k in range(len(a)):
    for i in range(51):
        if a[i] == 0:
            if a[i * 2] > 0 and a[i + 1] > 0:
                a[i] = max(a[i * 4], a[i + 1]) * (-1)
            if a[i * 2] < 0 or a[i + 1] < 0:
                a[i] = abs(min(a[i * 2], a[i + 1])) + 1
for i in range(0, 30):
    print(i, a[i])

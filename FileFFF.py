for a in range(1000):
    count = 0
    for x in range(1000):
        for y in range(1000):
            if (y + 3*x != 60) or (x > a) or (y > a):
                count += 1
    if count == 1000000:
        print(a)
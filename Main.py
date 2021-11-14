f = open("zadanie24_1.txt")
m = f.read()
r = [str(x) for x in m.split()]

counter = 0
maxcount = 0

i = 0
while i < len(r):
    if r[i] + r[i + 1] == 'AB':
        counter += 1
        i+=2
    else:
        if counter > maxcount:
            maxcount = counter
            counter = 0
print(maxcount)
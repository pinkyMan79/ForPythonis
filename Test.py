from math import sqrt
a = 244143
b = 1367821
for n in range(a, b + 1):
    ds = []
    if int(sqrt(n)) == sqrt(n):
      for d in range(2, int(sqrt(n))  + 1):
        if n % d == 0:
            ds.append(d)
            if d != n//d:
                ds.append(n//d)
            if len(ds) >= 3:
                break
      if len(ds) ==3:
        ds.sort()
        print( ds[1],ds[2])
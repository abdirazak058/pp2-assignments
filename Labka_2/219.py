# dorama epizodtaryn kosy:
n = int(input())
d = {}

for i in range(n):
    x, y = input().split()
    v = int(y)

    if x in d:
        d[x] += v
    
    else:
        d[x] = v

  #print(d)

for i in sorted(d):
    print(i, d[i])

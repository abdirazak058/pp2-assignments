#biregei kezdesken string index taby kerek:
n = int(input())
arr = []

for i in range(n):
    arr.append(input())

kai = []
for i in arr:
    if i not in kai:
        kai.append(i)
#print(*kai)

skai = sorted(kai)
for i in skai:
    print(i, arr.index(i) + 1)

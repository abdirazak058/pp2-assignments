#en kop kezdesetini:
n = int (input())
arr = list(map(int,input().split()))

s = {}

for i in arr:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1

#print(s)  

kez = 0
san = arr[0]

for i in arr:
    if s[i] > kez:
        kez = s[i]
        san = i
    elif s[i] == kez and i < san:
        san = i
print(san)

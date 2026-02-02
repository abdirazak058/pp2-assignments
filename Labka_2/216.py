n = int(input())
arr = list(map(int,input().split()))
tek = []

for i in arr:
    if i in tek:
        print("NO")
    else:
        print("YES")
    tek.append(i)


# max sandy minga aystry:
n = int(input())
arr = list(map(int,input().split()))

mx = max(arr)
mn = min(arr)

for i in range(len(arr)):
    if arr[i] == mx:
        arr[i] = mn

print(*arr)
# 3 birdei bolsa +1:
n = int(input())
arr = []
cout = 0
for i in range(n):
    arr.append(input())
                                     #print(*arr)
for i in range(n):
    bir = 0
    for j in range(n):
        if arr[i] == arr[j]:
            bir += 1
    if bir == 3:
        cout += 1
               



print(cout//3)
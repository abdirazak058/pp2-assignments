# neshe >0 san bar ekenin tabu kerek:
n = int(input())
arr = list(map(int,input().split()))
cout = 0
for i in arr:
    if i > 0:
        cout += 1
print(cout)

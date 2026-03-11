# Problem 606-514506. All Non-Negative
# Берілген массивте теріс сандар жоқпа тексеру!

a = int(input())
arr = list(map(int ,input().split()))

check = all(i >= 0 for i in arr) # all(Тізім) Тізімнің іші толық TRUE болса ғана TRUE болады!
#print(check)

if check:
    print("Yes")
else:
    print("No")
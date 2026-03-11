# Problem 601-514501. Sum of Squares
# Берілген сандарды жеке-жеке квадраттап қосу!

def sums (arr):
    total = 0
    for i in arr:
        total += (i**2)
    return total

a = int(input())
arr = list(map(int,input().split())) # map(функция, тізім!) тізімдегі әр әлеметке жеке жеке функция колданат!

print(sums(arr))
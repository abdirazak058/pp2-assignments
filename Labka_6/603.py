# Problem 603-514503. Index Each Word!
# Берілген сөздерге сәйкес индекстармен шығару керек 

a = int(input())
string = list((input().split()))

result = []

for i, index in enumerate(string): #enumerate(Тізім, индекс = нешеден басталу!) Тізімдегі әр әлементтке индекс береді!
    result.append(f"{i}:{index}")

print(" ".join(result))
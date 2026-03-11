# Problem 602-514502. Count Even Numbers 
# Берілген массивте жұп сандардың санын табу керек!

a = int(input())
arr = list(map(int, input().split()))

#result = filter(lambda x: x % 2 == 0, arr) 
#print(list(result)) # мына код жұп сандарды шығардады!

result = len(list(filter(lambda x: x % 2 == 0, arr))) # filter(Функция(True\False қайтаратын функция), тізім) Тізімдегі әр әлеметке жеке жеке Филтер колданат!
print(result)
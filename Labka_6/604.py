# Problem 604-514504. Dot Product
# Екі массивтің бірдей индексты сандарын көбейтіп бір массивке жинап сонын сумм тау керек!

a = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

#result = map(lambda x,y: x*y, arr1,arr2)
result = []

for x,y in zip(arr1,arr2): # Zip(Тізім_1, Тізім_2) Екі тізімнің ортак индекстегі элементтерін қосады!
    result.append(x * y)


print(sum(result))
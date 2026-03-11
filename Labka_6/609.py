# Problem 609-514509. Dictionary Query with Zip 
# Dictonary ішіне деректер енгізіп кеуді енгізгенде мәнін табу керек!

a = int(input())
keys = input().split()
values = input().split()

arr = dict(zip(keys, values)) 

find_letter = input()

print(arr.get(find_letter, "Not found"))
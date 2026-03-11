# Problem 607-514507. Longest Word
# Берілген сөлйем ішінен ұзын сөзді табу керек!

a = int (input())
sentence = list(input().split())

print(max(sentence, key = len)) # max(Тізім, key =  Тaбу керек тип))


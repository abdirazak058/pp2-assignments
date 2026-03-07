# Problem 509-512516. Count Three-Letter Words
# Берілген сөйлем ішінен 3 әріпті неше сөз бар екенін табу керек!

import re 

sentence = input()

words = re.findall(r"\b\w{3}\b", sentence) # "\b\w{3}\b" b degen sozdin basy jane aiagy w{3} degen 3 ccimboldan al degen

#print(words)
print(len(words))

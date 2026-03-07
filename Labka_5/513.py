# Problem 513-512521. Word Count With Regex
# Берілген сөйлем ішінде неше сөз бар екенің табу керек!

import re 

sentence = input()

words = re.findall(r"\w+" , sentence)

print(len(words))
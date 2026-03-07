# Problem 511-512518. Count Uppercase Letters
# Берілген сөйлем ішінде неше бас әріптер бар екенін тексеру!

import re 

sentence = input()

upper_list = re.findall(r"[A-Z]" , sentence)

#print(upper_list)
print(len(upper_list))
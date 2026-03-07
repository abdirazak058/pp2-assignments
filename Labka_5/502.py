# Problem 502-512509. Contains Substring
# Берілген сөйлемнің ішінде берілген сөз барма екенін тексеру!

import re

sentence = input()
find_word = input()

#print(type(sentence))
#print(type(find_word))

check = re.search(find_word, sentence)

if check:
    print("Yes")
else:
    print("No")
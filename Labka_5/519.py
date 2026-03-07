# Problem 519-512527. Word Count With Compiled Pattern
# Берілген сөйлемде қанша сөз бар екенін табу, брақ re.compile арқылы!

import re 

sentence = input()

simbol_r =  re.compile(r"\b\w+\b")
count_word = re.findall(simbol_r, sentence)

#print(count_word)
print(len(count_word))
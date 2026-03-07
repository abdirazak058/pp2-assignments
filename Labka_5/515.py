# Problem 515-512523. Double Every Digit
# Берілген сөзде сандарды әр қайсысын екі еселеп шығу керек!

import re 

word = input()

def two_digit(digit):
    return digit.group() * 2

new_word = re.sub(r"\d", two_digit, word)

print(new_word)
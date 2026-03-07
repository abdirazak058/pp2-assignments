# Problem 501: 512507. Starts With Hello
# Берілген сөйлем Hello сөзінен басталама тексеру!

import re

word = input()
check = re.match("Hello", word)

#print(check)
if check:
    print("Yes")
else:
    print("No")

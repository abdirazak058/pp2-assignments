# Problem 517-512525. Count Date-Like Patterns
# Берілген сөйлем ішінде неше уақыт(DATA) кездесетінін табу керек!

import re 

sentence = input()

digits = re.findall(r"\d{2}/\d{2}/\d{4}", sentence)

#print(digits)
if digits:
    print(len(digits))
else:
    print("0")

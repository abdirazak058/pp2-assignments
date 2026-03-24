# Problem 510-512517. Cat or Dog
# Берліген сөйлемнің ішінен Cat немесе Dog cөздері барма тексеру!

import re 

sentence = input()

check = re.search(r"cat|dog & Cat|Dog" , sentence)
#print(check)

if check:
    print("Yes")
else:
    print("No")
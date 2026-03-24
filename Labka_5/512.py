# Problem 512-512520. Sequences of Two or More Digits
# Берілген сөздің ішінде кездескен сандардан 2 таңбалыдан жоғарғысын алу керек!
import re 

word = input()

digits = re.findall(r"\d{2,}", word) 
print(*digits)
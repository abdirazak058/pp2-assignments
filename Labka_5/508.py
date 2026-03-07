# Problem 508-512515. Split by Pattern
# Берілген сөйлемнің ішінен берілген r" " символдарының орнына "," мен жазу керек 

import re 

sentence = input()
simbol_r = input()

new_sentence = re.split(simbol_r, sentence)
#print(new_sentence)
#new_sentence = ",".join(new_sentence)

print(",".join(new_sentence))

# Problem 518-512526. Literal Pattern Count
# БЕрілген сөзде қанша белгілі символ бар екенін табу!

import re 

word = input()
find_simbol = input()

simbol_r = re.escape(find_simbol)
count_simbol = re.findall(simbol_r, word)

#print(count_simbol)
print(len(count_simbol))
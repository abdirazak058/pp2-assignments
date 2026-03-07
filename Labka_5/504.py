# Problem 504-512511. Extract All Digits
# Берілген сөздің ішінен сандарды бөліп шығарып ттабу керек!

import re

word = input()

check = re.findall(r"\d", word) #findall tabady jane list jasaidy!

print(*check)
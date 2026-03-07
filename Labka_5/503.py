# Problem 503-512510. Count Pattern Matches
# Берілген сөйлемнің ішінде берліген сөз неше рет кездесетінін табу керек!

import re

sentence = input()
world = input()

count = re.findall(world, sentence)

#lenz = len(count)
print(len(count))
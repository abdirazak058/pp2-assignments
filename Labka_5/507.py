# Problem 507-512514. Replace All Occurrences
# Берліген сөйлемнен белгілі сөзді тауып берілген сөзге ауыстыру керек!

import re 

sentence = input()
find_world = input()
replec_world = input()

new_sentence = re.sub(find_world, replec_world, sentence) # re.sub degen sozdi tayup jana sozge ayustry

print(new_sentence)
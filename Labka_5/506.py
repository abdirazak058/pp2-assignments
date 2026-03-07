# Problem 506-512513. First Email-Like Substring
# Берілген сөйлемнен бірінші кездескен email ды шығару керек, егер болмаса No email шығару керек!

import re

world = input()

check = re.search(r"\S+@\S+\.\S+", world)
#print(check) #    <re.Match object; span=(0, 1), match='C'>

#print(check.group())  #group() degen ne - group degen bizde re.search() kaitargan mandi stringke ainalgyrady 

if check:
    print(check.group())
else:
    print("No email")
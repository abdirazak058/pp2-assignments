# Problem 505-512512. Starts With Letter, Ends With Digit
# Берілген сөздің басы әріппен, ал соңы санмен біту керек!

import re 

world = input()

check = re.match(r"^[A-Za-z].*[0-9]$", world)

if check:
    print("Yes")
else:
    print("No")
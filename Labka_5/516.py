# Problem 516-512524. Extract Name and Age
# Берілген сөйлемнен адам аты мен жасын бөліп алу!

import re 

information = input()

find_information = re.search(r"Name: (.+), Age: (\d+)", information)
#print(find_information)

if find_information:
    print(find_information.group(1), find_information.group(2))
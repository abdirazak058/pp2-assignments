# Problem 605-514505. Has a Vowel
# Сөзде тауысты дыбыс болса Yes шығару керек!

aa = input()
letters = ["A", "E", "I", "O", "U"," a", "e", "i", "o", "u"]

check = any(i in letters for i in aa) # any(Тізім)! Тізімніңішінде бір TRUE болса опши TRUE болып кайтады!

if check:
    print("Yes")
else:
    print("No")




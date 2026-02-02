n = int(input())
tek = True

while n != 0:
    a = n % 10
    if a % 2 == 1:
        tek = False
        break
    n //= 10

if tek:
    print("Valid")
else:
    print("Not valid")
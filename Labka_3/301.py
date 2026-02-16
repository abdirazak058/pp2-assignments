def tek (n):
    TF = True
    while n != 0:
        if (n % 10) % 2 == 1:
            TF = False
            break
        n //= 10
        #print(n)
    return TF
n = int(input())

if tek(n):
    print("Valid")
else:
    print("Not valid")

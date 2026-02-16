def men_krashpyn (n):
    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i

    if n == 1:
        print("Yes")
    else:
        print("No")

n = int(input())
men_krashpyn(n)
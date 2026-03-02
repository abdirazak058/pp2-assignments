#Squares from A to B (А ДАН В га дейинги сандардын квадратын шыгару)

def squares(a,b):
    for i in range(a, b + 1):
        yield i ** 2  # i * i Baskasha tasil

a, b = list(map(int, input().split()))
for x in squares(a, b):
    print(x)

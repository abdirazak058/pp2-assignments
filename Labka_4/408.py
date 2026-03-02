#Prime Numbers Range(Берилген санга дейинги прайм сандар)

import math
def prime(n):
    for num in range(2, n + 1):
        isprime = True
        for i in range(2, (num // 2) + 1): 
            if num % i == 0:
                isprime = False
                break
        if isprime:
            yield num
    
n = int(input())
for i in prime(n):
    print(i, end=" ")

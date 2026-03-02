# Divisibility Check (берилген сандарга дейин 3 ЖАНЕ 4 ке болинетин сандарды шыгару )

def bolinet(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
n = int(input())
for i in bolinet(n):
    print(i, end=" ")
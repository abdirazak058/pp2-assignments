# Squares of Numbers(Санды квадраттау)

def s(n):
    for i in range(1, n + 1):
        yield i * i  # i **2 Baskasha tasil

n = int(input())
for Kbadrat in s(n):
    print(Kbadrat)
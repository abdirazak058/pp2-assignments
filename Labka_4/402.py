# Even Numbers Generator (Жуп сандарды геренаторлау)

n = int(input())
def zhup(n):
    for i in range(0, n + 1, 2):
        yield i

for ev in zhup(n):
    if ev != 0:
        print(",", end = "")
    print(ev, end=" ")

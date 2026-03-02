#Powers of Two (2 нин дарежеси)
def powww(n):
    for i in range(n + 1):
        yield 2 ** i

n = int(input())
for p in powww(n):
    print(p, end = " ")

def ret(a, k):
    yield a * k

a = input().split()
k = int(input())
for i in ret(a, k):
    print(*i)

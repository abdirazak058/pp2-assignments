#The Countdown (Берилген саннан кери журу)

def count_down(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for c in count_down(n):
    print(c)  # print(c, end = " ")
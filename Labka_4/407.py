#Reverse Iterator (Көтінен керсінше)
def reverse(n):
    yield n[::-1]
    
n = input()
for i in reverse(n):
    print(i)

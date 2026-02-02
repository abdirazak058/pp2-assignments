#jai sanba teksery:
n = int(input())
ass = True

for i in range(2,n):
    if n % i == 0:
        ass = False
        break
if ass:
    print("YES")
else:
    print("NO")
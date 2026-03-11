# Problem 610-514510. Count Truthy Numbers
# Берілген массив ішінен 0 < сандарды табу керек нешеу екенін!
a = int(input())
arr = list(map(int, input().split()))

result = map(bool, arr)
#print(list(result))

print(sum(result))
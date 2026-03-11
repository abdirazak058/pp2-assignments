# Problem 608-514508. Sorted Unique Numbers
# Берілген массив ішінен қайталанатындарын өшіріп қайталанбайтындарын өсу ретімен шығару!

a = int(input())
arr = list(map(int, input().split()))

result = set(arr) # Берегей мәнді қабылдайды!
print(*(sorted(result)))
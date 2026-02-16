def money (n,m):
    if n >= m:
        print(n - m)
    else:
        print("Insufficient Funds")
        
aibar, pororo = map(int, input().split())
money(aibar, pororo)

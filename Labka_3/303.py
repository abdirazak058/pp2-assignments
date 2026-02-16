s = input().strip()
to_san = {
    "ZER": "0",
    "ONE": "1", 
    "TWO": "2", 
    "THR": "3", 
    "FOU": "4",
    "FIV": "5", 
    "SIX": "6", 
    "SEV": "7", 
    "EIG": "8", 
    "NIN": "9"
}
to_soz = {v: k for k, v in to_san.items()}

for i in ['+', '-', '*']:
    if i in s:
        left, right = s.split(i)
        oper = i
        break

def soz_to_san(word):
    saan = ""
    i = 0
    while i < len(word):
        part = word[i:i+3]
        saan += to_san[part]
        i += 3
    return int(saan)


a = soz_to_san(left)
b = soz_to_san(right)

if oper == '+':
    result = a + b
elif oper == '-':
    result = a - b
else:
    result = a * b

ans = ""
for d in str(result):
    ans += to_soz[d]

print(ans)

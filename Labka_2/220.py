# ?:
import sys
input = sys.stdin.readline
n = int(input())
db = {}
out = []

for _ in range(n):
    l = input().rstrip('\n')

    if l.startswith("set"):
        p = l.split(maxsplit=2)
        key = p[1]
        v = p[2] if len(p) == 3 else ""
        db[key] = v

    else:  
        key = l.split()[1]
        if key in db:
            out.append(db[key])
        else:
            out.append(f"KE: no key {key} found in the document")

sys.stdout.write("\n".join(out))
#JSON Patch Update (Мандерин озгертеди НОН бол алып баск аболса озгертеди!)

import json #JavaScript Object Notation

def a_p(s, p):
    for key, value in p.items():
        if value is None:
            s.pop(key, None)
        elif key in s and isinstance(s[key], dict) and isinstance(value, dict):
            a_p(s[key], value)
        else:
            s[key] = value
    return s


s = json.loads(input())
p= json.loads(input())

res = a_p(s, p)

print(json.dumps(res, separators=(',', ':'), sort_keys=True))

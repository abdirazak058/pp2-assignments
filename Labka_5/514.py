# Problem 514-512522. Digits Only With Compile
# БЕрілген сөзде басынан аяағына дейін сан ба тексеру!
 
import re 

word = input()

simbol_r = re.compile(r"^\d+$")
check = simbol_r.match(word)

#print(check)

if check:
    print("Match")
else:
    print("No match")
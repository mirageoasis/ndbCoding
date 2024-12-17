string=input()

now=""

for s in string:
    if s == "U":
        if now == "":
            now+="U"
    
    if s == "C":
        if now == "U":
            now+="C"
        if now == "UCP":
            now+="C"
    if s == "P":
        if now == "UC":
            now+="P"

print("I love UCPC" if now == "UCPC" else "I hate UCPC")
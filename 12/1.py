string=input("")

first = sum([int(i) for i in string[:len(string) // 2]])
second = sum([int(i) for i in string[len(string) // 2:]])

if first == second:
    print("LUCKY")
else:
    print("READY")
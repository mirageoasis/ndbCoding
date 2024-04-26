N = input()

tar = 'UCPC'

for i in N:
    if not tar:
        break
    if i == tar[0]:
        tar = tar[1:]

if tar:
    print("I hate UCPC")
else:
    print("I love UCPC")
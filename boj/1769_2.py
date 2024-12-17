# 한자리 수로 만들기

s=int(input())

convert=0
while True:
    if len(str(s)) == 1:
        print(convert)
        print("YES" if s % 3 == 0 else "NO")
        break
    
    s=sum([int(i) for i in str(s)])
    convert+=1
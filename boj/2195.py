s=input()
p=input()
# 딱히 뭐가 없음 
start = 0
cnt=0
for i in range(len(p)):
    # contains
    substr = p[start:i+1]
    #print(start, i+1)
    #print(substr)
    if substr in s:
        continue
    else:
        #print("copy")
        start=i
        cnt+=1
cnt+=1
print(cnt)
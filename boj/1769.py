N = input()

ans=0
while len(N) > 1:
    ans+=1
    N = str(sum([int(i) for i in N]))

print(ans)
if N in ["3", "6", "9"]:
    print("YES")
else:
    print("NO")
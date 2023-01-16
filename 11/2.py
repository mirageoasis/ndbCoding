#02984
#

li=input()

ans=0

for i in li:
    num = int(i)
    ans = max(ans*num, ans+num)
print(ans)
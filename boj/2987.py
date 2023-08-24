a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

N = int(input())
ans = 0

def in_n_out(d1, d2):
    one = abs(d1 * (b2 - c2) + b1 * (c2 - d2) + c1 * (d2 - b2)) / 2 # a 제외
    two = abs(a1 * (d2 - c2) + d1 * (c2 - a2) + c1 * (a2 - d2)) / 2 # b 제외
    three = abs(a1 * (b2 - d2) + b1 * (d2 - a2) + d1 * (a2 - b2)) / 2 # c 제외

    return one + two + three == wide
    

wide = abs(a1 * (b2 - c2) + b1 * (c2 - a2) + c1 * (a2 - b2)) / 2

for i in range(N):
    d1, d2 = map(int, input().split())
    
    if in_n_out(d1, d2):
        ans+=1


print(wide)
print(ans)
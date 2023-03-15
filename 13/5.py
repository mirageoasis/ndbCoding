N = input().split()
li = list(map(int ,input().split()))
plus, minus, mul, div = map(int ,input().split())

mini = 1000000000000
maxi = -1000000000000

def rec(plus, minus, mul, div, li, idx, val):
    global mini
    global maxi

    if(idx == len(li)):
        mini = min(mini, val)
        maxi = max(maxi, val)
        #print(val)

    if (plus > 0):
        rec(plus-1, minus, mul, div, li, idx+1, val+li[idx])
    if(minus > 0):
        rec(plus, minus-1, mul, div, li, idx+1, val-li[idx])
    if(mul > 0):
        rec(plus, minus, mul-1, div, li, idx+1, val * li[idx])
    if(div > 0):
        if (val < 0):
            rec(plus, minus, mul, div-1, li, idx+1, -(abs(val) // li[idx]))            
        else:
            rec(plus, minus, mul, div-1, li, idx+1, val // li[idx])

    
rec(plus, minus, mul, div, li, 1, li[0])

#rec()

print(maxi)
print(mini)

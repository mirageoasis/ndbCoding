## zero
# one
# two
# three
# four
# five
## six
# seven
## eight
# nine
from collections import defaultdict

N=int(input())

def func(k, s):
    #$print(s)
    d = defaultdict(int)
    for i in s:
        d[i]+=1
    ans=''
    
    while d['z'] > 0:
        ans+='0'
        d['z']-=1
        d['e']-=1
        d['r']-=1
        d['o']-=1

    while d['x'] > 0:
        ans+='6'
        d['s']-=1
        d['i']-=1
        d['x']-=1

    while d['g'] > 0:
        ans+='8'
        d['e']-=1
        d['i']-=1
        d['g']-=1
        d['h']-=1
        d['t']-=1

    while d['s'] > 0:
        ans+='7'
        d['s']-=1
        d['e']-=1
        d['v']-=1
        d['e']-=1
        d['n']-=1

    while d['v'] > 0:
        ans+='5'
        d['f']-=1
        d['i']-=1
        d['v']-=1
        d['e']-=1

    while d['f'] > 0:
        ans+='4'
        d['f']-=1
        d['o']-=1
        d['u']-=1
        d['r']-=1

    while d['i'] > 0:
        ans+='9'
        d['n']-=1
        d['i']-=1
        d['n']-=1
        d['e']-=1

    while d['w'] > 0:
        ans+='2'
        d['t']-=1
        d['w']-=1
        d['o']-=1


    while d['r'] > 0:
        ans+='3'
        d['t']-=1
        d['h']-=1
        d['r']-=1
        d['e']-=2
    
    while d['o'] > 0:
        ans+='1'
        d['o']-=1
        d['n']-=1
        d['e']-=1

    print(f"Case #{k+1}: {''.join(sorted(ans))}")

for i in range(N):
    s=input()
    func(i, s.lower())
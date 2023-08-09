LIM = 9999999999

result = [-LIM, LIM]

N=input()

def counter(string):
    cnt = 0
    for i in string:
        if int(i) % 2 != 0:
            cnt+=1
    return cnt

def adder(args):
    ret = 0
    for i in args:
        ret+=int(i)
    return str(ret)

def cal(N, prev):
    if len(N) == 1:
        result[0] = max(result[0], prev + counter(N)) 
        result[1] = min(result[1], prev + counter(N)) 
    elif len(N) == 2:
        cal(adder([N[0], N[1]]), prev + counter(N))
    else:
        for i in range(1 , len(N) - 1):
            for j in range(i + 1, len(N)):
                cal(adder([N[0:i], N[i:j], N[j:]]), prev + counter(N))


cal(N, 0)

print(result[1], result[0])
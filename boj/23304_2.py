s=input()

def if_pan(string):
    if len(string) == 1:
        return True
    for i in range(0, len(string)):
        if string[i] != string[len(string)-i-1]:
            return False    
    front=string[:len(string)//2]
    back=""
    if len(string) % 2 ==0:
        back=string[len(string)//2:]
    else:
        back=string[len(string)//2+1:]
    return if_pan(front) & if_pan(back)

if len(s) == 1:
    print("AKARAKA")
else:
    flag=True

    flag=if_pan(s)

    if flag:
        print("AKARAKA")
    else:
        print("IPSELENTI")
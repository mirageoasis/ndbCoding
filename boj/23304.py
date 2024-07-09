# 분할 정복?


string=input()

def div(string):
    #print(string[start:end+1])
    if len(string) == 1:
        return True

    mid=len(string) // 2
    #print(mid)

    if len(string) % 2 == 0:
        left=string[:mid]
        right=string[mid:]
    else:
        left=string[:mid]
        right=string[mid+1:]
    if left == right:
        return div(left) and div(right)
    else:
        return False



if div(string):
    print("AKARAKA")
else:
    print("IPSELENTI")
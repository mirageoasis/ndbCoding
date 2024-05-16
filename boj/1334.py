N=int(input())

def convert_new(N):
    n_list = list(str(N))

    for i in range(len(n_list)//2+1):
        n_list[len(n_list)-1-i]=n_list[i]
    
    return int(''.join(n_list))


def all_nine(N):
    for i in N:
        if i != '9':
            return False
    return True

if all_nine(str(N)):
    print(N+2)
else:
    new_number=convert_new(N)
    if new_number > N:
        print(new_number)
    else:
        n_list=list(str(N))
        n_len=len(str(N))
        mid=n_len//2
        if n_list[mid] != '9':
            if n_len % 2 == 0:
                mid-=1
            t=str(int(n_list[mid])+1)
            # print(t)
            # print(n_list)
            # print(n_list[mid])
            n_list[mid]=t
            # print(n_list)
            print(convert_new(int(''.join(n_list))))
        else:
            t=int(''.join(n_list[:mid]))
            t+=1
            n_list[mid]='0'
            for idx, i in enumerate(str(t)):
                n_list[idx]=i
            
            #print(n_list)
            print(convert_new(int(''.join(n_list))))
string = input()

now=string[0]
first=string[0]

if len(string) == 1:
    print(0)
else:
    same_cnt=1
    new_str=string[0]
    for i in string[1:]:
        if i != now:
            now=i
            new_str+=i
            if first == i:
                same_cnt+=1
    #print(new_str)
    #print(same_cnt)
    print(min(len(new_str) - same_cnt, same_cnt))

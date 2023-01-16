def cal(s, length):
    start_idx=0
    end_idx=length
    current=s[start_idx:end_idx]
    start_idx=end_idx
    end_idx=length*2    
    new_str=""    
    
    count=1
    while end_idx <= len(s):
        
        if current==s[start_idx:end_idx]:
            count+=1
        else:
            if count != 1:
                new_str+=str(count)
            
            new_str+=current    
            current=s[start_idx:end_idx]
            count=1
    
    if current==s[start_idx:end_idx]:
        count+=1
    else:
        if count != 1:
            new_str+=str(count)

        new_str+=current    
        current=s[start_idx:end_idx]
        count=1
        
        start_idx=end_idx
        end_idx+=length
    
    new_str+=current
    
    return new_str

def solution(s):
    answer = len(s)
    
    for i in range(len(s) // 2):
        answer = min(answer, cal(s, i))    
        
    return answer

string=input("")

solution(string)
chart=[]

string=input()

ans=0
flag=True
for s in string:
    if s == "q":
        for i in range(len(chart)):
            now_string=chart[i]
            if not now_string:
                chart[i]+="q"
                break
        else:
            chart.append("q")
    elif s == "u":
        for i in range(len(chart)):
            now_string=chart[i]
            if now_string and now_string[-1] == "q":
                chart[i]+="u"
                break
        else:
            flag=False
            break
    
    elif s == "a":
        for i in range(len(chart)):
            now_string=chart[i]
            if now_string and now_string[-1] == "u":
                chart[i]+="a"
                break
        else:
            flag=False
            break
    
    elif s == "c":
        for i in range(len(chart)):
            now_string=chart[i]
            if now_string and now_string[-1] == "a":
                chart[i]+="c"
                break
        else:
            flag=False
            break
    
    elif s == "u":
        for i in range(len(chart)):
            now_string=chart[i]
            if now_string and now_string[-1] == "q":
                chart[i]+="u"
                break
        else:
            flag=False
            break
    
    elif s == "k":
        for i in range(len(chart)):
            now_string=chart[i]
            if now_string and now_string[-1] == "c":
                chart[i]=""
                ans=max(ans, i)
                break
        else:
            flag=False
            break
#print(flag)
for c in chart:
    #print(c)
    if c:
        flag=False

print(ans+1 if flag else -1)
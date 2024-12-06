n=int(input())

for i in range(n):
    m, n, year, month = map(int, input().split())

    first_year=year
    first_month=year
    start_count=year
    if year > n:
        first_month=year%n if year%n else n
    sub=n - m
    flag=True
    while start_count <= m*n:
        #print(first_year, first_month, start_count)
        if (first_year, first_month) == (year, month):
            print(start_count)
            flag=False
            break
        
        first_year= (first_year+m)%m if (first_year+m)%m else m
        first_month= (first_month+n-sub)%n if (first_month+n-sub)%n else n
        start_count+=m
    
    if flag:
        print(-1)
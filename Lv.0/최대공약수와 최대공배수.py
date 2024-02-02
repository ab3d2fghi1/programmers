def solution(n, m):
    answer = ['','']
    a=[]
    b=[]
    for i in range(1,n+1):
        if n%i==0: a.append(i)
    for j in range(1,m+1):
        if m%j==0: b.append(j)
    count=[]
    for k in range(len(a)):
        for l in range(len(b)):
            if a[k]==b[l]: count.append(a[k])
    answer[0]=max(count)
    if n%m==0: answer[1]=n
    elif m%n==0: answer[1]=m
    else:
        answer[1]=(n*m)/answer[0]
    return answer

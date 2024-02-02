def solution(n):
    cnt=1
    num=[]
    while len(num)!=n:
        if '3' not in str(cnt) and cnt%3!=0: num.append(cnt)
        cnt+=1
    return num[n-1]

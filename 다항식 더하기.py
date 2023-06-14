def solution(polynomial):
    answer = ''
    polynomial=list(polynomial.split())
    cal_cnt=0
    cal=[]
    for i in polynomial:
        if i=='+': cal.append('+')
        elif i=='-': cal.append('-')
    x_cnt=0
    num_cnt=0
    for j in range(0,len(polynomial)):
        if 'x' in polynomial[j]:
            if j==0 or cal[cal_cnt]=='+':
                if polynomial[j]=='x': x_cnt+=1
                else: x_cnt+=int(polynomial[j][:-1])
                if j!=0: cal_cnt+=1
            elif cal[cal_cnt]=='-':
                if polynomial[j]=='x': x_cnt-=1
                else: x_cnt-=int(polynomial[j][:-1])
                cal_cnt+=1
        elif polynomial[j].isnumeric()==True:
            if j==0: num_cnt+=int(polynomial[j])
            else:
                if cal[cal_cnt]=='+': num_cnt+=int(polynomial[j])
                elif cal[cal_cnt]=='-': num_cnt-=int(polynomial[j])
                cal_cnt+=1
    num_cnt=str(num_cnt)
    x_cnt=str(x_cnt)
    if x_cnt=='0': answer=num_cnt
    elif num_cnt=='0':
        if x_cnt=='1': answer='x'
        else: answer=x_cnt+'x'
    elif int(num_cnt)>0: 
        if x_cnt=='1': answer='x'+' '+'+'+' '+num_cnt
        else: answer=x_cnt+'x'+' '+'+'+' '+num_cnt
    elif int(num_cnt)<0:
        if x_cnt=='1': answer='x'+' '+'-'+' '+num_cnt[-1]
        else: answer=x_cnt+'x'+' '+'-'+' '+num_cnt[-1]
    return answer

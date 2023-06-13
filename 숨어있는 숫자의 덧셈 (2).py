def solution(my_string):
    num=''
    for i in my_string:
        if i.isalpha()==True: num+=' '
        elif i.isdigit()==True: num+=i
    num=num.split()
    num=map(int,num)
    return sum(num)

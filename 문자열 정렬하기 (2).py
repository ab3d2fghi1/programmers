def solution(my_string):
    answer=''
    for i in my_string:
        if i.isupper()==True: 
            answer+=i.lower()
        else: answer+=i
    answer=list(answer)
    answer.sort()
    return ''.join(answer)

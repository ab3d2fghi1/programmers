def solution(my_string):
    answer=[]
    for i in my_string:
        if i.isalpha()==False: answer.append(i)
    answer=list(map(int,answer))
    result=0
    for j in answer:
        result=j+result
    return result

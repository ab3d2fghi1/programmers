def solution(my_string):
    li=my_string.split()
    answer=0
    answer+=int(li[0])
    for i in range(1,len(li)):
        if li[i]=='+':
            i+=1
            answer+=int(li[i])
        elif li[i]=='-':
            i+=1
            answer-=int(li[i])
    return answer

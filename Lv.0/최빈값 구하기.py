def solution(array):
    answer = {}
    for i in range(0,max(array)+1):
        count=0
        for j in range(len(array)):
            if i==array[j]:
                count+=1
        answer[i]=count
    ky=list(answer.keys())
    vl=list(answer.values())
    num=0
    result=0
    for j in range(len(answer)):
        if vl[j]==max(vl):
            num+=1
            result=ky[j]
    if num==1: return result
    else: return -1

def solution(num, k):
    num=str(num)
    num=list(map(int,num))
    answer=[]
    for i in range(len(num)):
        if num[i]==k: answer.append(i+1)
    if len(answer)>0: return answer[0]
    else: return -1

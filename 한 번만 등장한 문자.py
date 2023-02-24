def solution(s):
    alpha =[chr(i) for i in range(97,123)]
    s=list(s)
    answer = ''
    for i in alpha:
        count=0
        for j in s:
            if i==j: count+=1
        if count==1: answer+=i
    return answer

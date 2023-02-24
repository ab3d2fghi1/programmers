def solution(s):
    s=list(s)
    answer=['']
    count=0
    for i in range(len(s)):
        if s[i]==' ':
            count+=1
            answer.append('')
        else: answer[count]+=s[i]
    answer=list(map(int,answer))
    return str(min(answer))+' '+str(max(answer))

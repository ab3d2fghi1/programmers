def solution(quiz):
    answer = []
    for i in quiz:
        k=i.split()
        num=0
        num+=int(k[0])
        for j in range(1,len(k)):
            if k[j]=='+':
                j+=1
                num+=int(k[j])
            elif k[j]=='-':
                j+=1
                num-=int(k[j])
            elif k[j]=='=':
                j+=1
                if num==int(k[j]):answer.append("O")
                else: answer.append("X")
    return answer

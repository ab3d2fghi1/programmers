def solution(s):
    s=list(s)
    answer=''
    trans=[]
    for i in range(len(s)):
        if s[i].isalpha()==True:
            trans.append(s[i])
        elif s[i]==' ':
            if len(trans)>0:
                for j in range(len(trans)):
                    if j%2==0: trans[j]=trans[j].upper()
                    elif j%2!=0: trans[j]=trans[j].lower()
                answer+=''.join(trans)
                answer+=' '
                trans=[]
            else: answer+=' '
    for k in range(len(trans)):
        if k%2==0: trans[k]=trans[k].upper()
        elif k%2!=0: trans[k]=trans[k].lower()
    answer+=''.join(trans)
    return answer

def solution(emergency):
    sample=[]
    for x in range(len(emergency)):
        sample.append(emergency[x])
    sample.sort(reverse=True)
    answer=[]
    for y in range(len(emergency)):
        answer.append('')
    for i in range(len(sample)):
        for j in range(len(emergency)):
            if sample[i]==emergency[j]:
                answer[j]=i+1
    return answer

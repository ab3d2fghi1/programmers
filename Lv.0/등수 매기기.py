def solution(score):
    mean_score=[]
    score_sort=[]
    answer=[]
    for i in score:
        mean_score.append(sum(i)/2)
        score_sort.append(sum(i)/2)
    score_sort.sort(reverse=True)
    for j in mean_score:
        answer.append(score_sort.index(j)+1)
    return answer

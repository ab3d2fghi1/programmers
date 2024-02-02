def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        n=str(n)
        n=list(n)
        for l in n:
            if l==str(k): answer+=1
    return answer

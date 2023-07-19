def solution(M, N):
    paper=[M,N]
    answer=(min(paper)-1)+min(paper)*(max(paper)-1)
    return answer

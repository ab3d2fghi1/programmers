def solution(bin1, bin2):
    x=int(bin1,2)
    y=int(bin2,2)
    answer=bin(x+y)
    return answer[2:]

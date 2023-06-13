def solution(array):
    answer = 0
    for i in array:
        i=list(str(i))
        answer+=i.count('7')
    return answer

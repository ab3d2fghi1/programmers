def solution(array, n):
    num=[]
    for i in array:
        if n>i: num.append(n-i)
        else: num.append(i-n)
    answer=[]
    for j in range(len(num)):
        if num[j]==min(num): answer.append(array[j])
    return min(answer)

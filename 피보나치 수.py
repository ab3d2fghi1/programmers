def solution(n):
    count=[0,1]
    for j in range(2,n+1):
        count.append(count[j-2]+count[j-1])
    return count[n]%1234567

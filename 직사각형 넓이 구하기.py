def solution(dots):
    answer=0
    length=[]
    for i in range(1,len(dots)):
        length.append(((dots[i][0]-dots[0][0])**2)**(1/2)+((dots[i][1]-dots[0][1])**2)**(1/2))
    length.remove(max(length))
    answer=length[0]*length[1]
    return answer

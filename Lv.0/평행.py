def solution(dots):
    answer=0
    [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]=dots
    l_12=abs((y2-y1)/(x2-x1))
    l_34=abs((y4-y3)/(x4-x3))
    l_23=abs((y3-y2)/(x3-x2))
    l_14=abs((y4-y1)/(x4-x1))
    if l_12==l_34 or l_23==l_14: answer=1
    return answer

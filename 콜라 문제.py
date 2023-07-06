import sys
sys.setrecursionlimit(10000)
def solution(a, b, n):
    answer=0
    def recurision(coke):
        if coke<a or coke//a==0: return
        nonlocal answer
        answer+=coke//a*b
        recurision((coke//a)*b+coke%a)
    recurision(n)
    return answer

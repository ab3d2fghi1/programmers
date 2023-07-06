import sys
sys.setrecursionlimit(10000)
def solution(a, b, n):
    answer=0
    def recursion(coke):
        if coke<a or coke//a==0: return
        nonlocal answer
        answer+=coke//a*b
        recursion((coke//a)*b+coke%a)
    recursion(n)
    return answer

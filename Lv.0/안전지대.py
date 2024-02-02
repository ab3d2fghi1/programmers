def solution(board):
    n=len(board)
    sx=[-1,1,0,0,-1,-1,1,1]
    sy=[0,0,-1,1,-1,1,-1,1]
    location=[]
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j]==1:
                location.append([i,j])
    for x,y in location:
        for i in range(0,8):
            if 0 <= (x+sx[i]) <n and 0<= (y+sy[i]) <n: board[x+sx[i]][y+sy[i]]=1
    answer=0
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j]==0: answer+=1
    return answer

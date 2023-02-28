def solution(before, after):
    before=list(before)
    before.sort()
    after=list(after)
    after.sort()
    for i in range(len(before)):
        if before[i]==after[i]: pass
        else: return 0
    return 1

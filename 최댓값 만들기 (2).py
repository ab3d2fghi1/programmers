def solution(numbers):
    answer=min(numbers)*max(numbers)
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if (numbers[i]*numbers[j])>answer: answer=(numbers[i]*numbers[j])
    return answer

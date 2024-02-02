def solution(numbers):
    num_list=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(num_list)):
        if num_list[i] in numbers: numbers=numbers.replace(num_list[i],str(i))
    numbers=int(numbers)
    return numbers

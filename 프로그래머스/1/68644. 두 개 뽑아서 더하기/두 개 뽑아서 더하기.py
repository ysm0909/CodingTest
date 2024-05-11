def solution(numbers):
    answer = []
    num = {} 
    for i in numbers:
        if(i not in num):
            num[i] = False
        elif(i in num):
            if(num[i] == False):
                num[i] = True

    for one in num.keys():
        if(num[one] == True):
            num[one] = False
            answer.append((2 * one))

    num_list = list(num.keys())

    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if((num_list[i] + num_list[j]) not in answer):
                answer.append(num_list[i] + num_list[j])

    answer.sort()
    return answer
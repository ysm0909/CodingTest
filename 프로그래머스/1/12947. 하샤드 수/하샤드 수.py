def solution(x):
    digit_sum = sum(int(digit) for digit in str(x))
    answer = x % digit_sum == 0
    return answer
def solution(phone_number):
    masked = '*' * (len(phone_number) - 4)
    remains = phone_number[-4:]
    answer = masked + remains
    return answer
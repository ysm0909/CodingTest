def solution(n):
    n = int(n)
    temp = map(str, str(n))
    answer = int(''.join(sorted(temp, reverse = True)))
    return answer
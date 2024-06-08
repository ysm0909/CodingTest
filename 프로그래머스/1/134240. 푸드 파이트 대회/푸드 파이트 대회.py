def solution(food):
    n = len(food)
    half_max = [food[i] // 2 for i in range(1, n)]  # 물 제외한 각 음식의 반을 계산
    
    # 음식 배치를 위한 초기 문자열 구성
    # 물을 제외하고 각 음식을 최대 사용 가능 개수만큼 배치
    base_sequence = ""
    for i in range(1, n):
        base_sequence += str(i) * half_max[i - 1]
    
    # 중앙의 물(0번 음식)과 함께 대칭적으로 배치
    final_sequence = base_sequence + "0" + base_sequence[::-1]
    
    return final_sequence

# 예제 입력에 대한 테스트
print(solution([1, 3, 4, 6]))  # "1223330333221"
print(solution([1, 7, 1, 2]))  # "111303111"

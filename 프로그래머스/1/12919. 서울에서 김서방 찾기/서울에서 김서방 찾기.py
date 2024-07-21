def solution(seoul):
    num = 0
    for i in seoul:
        if i == "Kim":
            break
        num += 1
        
    answer = f"김서방은 {num}에 있다"
    
    return answer


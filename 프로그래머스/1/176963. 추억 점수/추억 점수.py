def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for i in range(len(photo)):
        tmp = 0
        for k,v in dic.items():
            if k in photo[i]:
                tmp += v
        answer.append(tmp)
    return answer
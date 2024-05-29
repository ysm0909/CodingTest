def solution(s):
    dct = {}
    lst = []

    for i, c in enumerate(s):
        try:
            index = dct[c]
            lst.append(i - index)
            dct[c] = i
        except:
            dct[c] = i
            lst.append(-1)
    return lst
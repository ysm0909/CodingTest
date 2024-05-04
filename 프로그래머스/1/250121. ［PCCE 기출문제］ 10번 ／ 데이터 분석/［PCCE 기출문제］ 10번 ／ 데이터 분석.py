def solution(data, ext, val_ext, sort_by):
    # 데이터 필터링
    filtered_data = [item for item in data if item[data_columns[ext]] < val_ext]
    
    # 필터링된 데이터 정렬
    sorted_data = sorted(filtered_data, key=lambda x: x[data_columns[sort_by]])
    
    return sorted_data

# 인덱스 매핑
data_columns = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
print(solution(data, "date", 20300501, "remain"))  # 출력: [[3, 20300401, 10, 8], [1, 20300104, 100, 80]]

# 파일이름 : 4주차 미션
# 작 성 자 : 60232294 신지웅

#미션 3
bucket_list = []

bucket_list.append(input("맛집 리스트 입력: "))
bucket_list.append(input("맛집 리스트 입력: "))
bucket_list.append(input("맛집 리스트 입력: "))

print("리스트:", bucket_list)

bucket_list.insert(0, input("맛집 리스트 추가: "))
print("리스트:", bucket_list)

bucket_list.remove(input("도장 깨기: "))
print("리스트:", bucket_list)

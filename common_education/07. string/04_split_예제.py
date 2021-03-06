# 04_split_예제.py

# 아래와 같은 데이터가 입력되었을 때 숫자만 추출해서 총 합계를 구하시오
str_data = "{a1:20},{a2:30},{a3:15},\
        {a4:50},{a5:-14},{a6:15},\
        {a7:20},{a8:70},{a9:-100}"

# 데이터를 분리할 구분자를 결정 - 각각 데이터로 분리(,를 구분자로 사용)
split_str_data = str_data.split(',')
print(split_str_data) # '[a1:20]' 리스트 내 하나의 요소(데이터)
# 콜론을 기준으로 숫자가 포함되어 있는애/ 포함되어있지 않은애를 구분
# print(split_str_data[0].split(':')[1]) # 쪼갠 상태에서 바로 인덱싱 -> 20만 가져와라
# print(split_str_data[0].split(':')[1].split(']')[0]) # 20과 ]를 쪼개서 20만 가져와라

# 숫자만 추출한 후 누적 합산
tot = 0  # 누적변수
for i in range(0, len(split_str_data)) :
    temp = split_str_data[i].split(':')[1].split('}')[0]  # 추출결과 문자열
    # : 콜론을 기준으로 분리해서 오른쪽 추출
    # } 괄호를 기준으로 분리해서 왼쪽 숫자만 추출
    # 누적합산
    tot += int(temp)

print('추출된 숫자의 합은 %d 입니다.' % tot)



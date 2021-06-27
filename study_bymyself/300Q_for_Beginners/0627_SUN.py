# 0627_SUN.py

# 051. 리스트 생성
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 052. 리스트에 원소 추가
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# 리스트에 원소를 추가하는 메소드: 변수명.append(추가할 내용)
movie_rank.append('배트맨')
print(movie_rank)

# 053. 리스트의 특정 순서에 원소 추가
movie_rank.insert(1, '슈퍼맨')
# insert(인덱스, 원소) 메소드를 사용하면 특정 위치에 값을 끼워 넣을 수 있음
print(movie_rank)

# 054. 리스트에서 특정 원소만 삭제
del movie_rank[3]
print(movie_rank)

# 055. 리스트에서 특정 원소 2개 이상 삭제
del movie_rank[2]
del movie_rank[2]
# 리스트에서 어떤 값을 삭제하면, 남은 값들은 새로 인덱싱 됨
# 따라서 여러 값을 삭제할 때는 어떤 값을 먼저 삭제한 후 남은 원소들에 대해 순서를 새로 고려하여 삭제해야 함

# 056. langs 리스트 만들기
lang1 = ['C', 'C++', 'JAVA']
lang2 = ['Python', 'Go', 'Cc']
# 문제에는 lang2 리스트의 마지막 원소가 C#라는 식별자로 되어 있는데 이것은 주석 기호 때문에 인식이 안 됨...
langs = lang1 + lang2
print(langs)
# 두 리스트를 더하면 하나의 리스트로 만들 수 있음

# 057. 리스트에서 최솟값, 최댓값 출력
nums = [1, 2, 3, 4, 5, 6, 7]
a = max(nums)
b = min(nums)
print('max: ', a)
print('min: ', b)

# 058. 리스트의 합 출력
nums = [1, 2, 3, 4, 5]
print(sum(nums))
# sum() 함수를 사용하면 변수의 값을 모두 더한다

# 059. 리스트에 저장된 데이터의 개수 구하기
cook = ['피자', '김밥', '만두', '양념치킨', '족발', '피자', '김치만두', '쫄면', '쏘세지', '라면', '팥빙수', '김치전']
print(len(cook))
# len() 함수는 매개변수로 들어온 문자열의 길이를 반환함
# 내부에 있는 문자의 개수 및 공백을 포함하여 카운팅하여 반환해주는 함수임
# 출처 https://redcow77.tistory.com/357

# 060. 리스트의 평균 출력
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums) # 리스트 내 원소들의 합 / 리스트 내 원소들의 개수
print(average)  # 따로 평균을 내는 함수가 없어서 직접 계산해야 함!

print('------------------------------------')

# 061. 슬라이싱을 사용한 출력
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062. 슬라이싱을 사용한 출력2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0::2])

# 063. 슬라이싱을 사용한 출력3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 064. 슬라이싱을 사용한 출력4
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 065. 리스트 내 특정 요소만 출력
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], end=" ")
print(interest[2])

# 066. join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# ".join(리스트) 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환
# '구분자'.join(리스트) 함수로 실행하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줌
# 출처: https://blockdmask.tistory.com/468
print(" ".join(interest))

# 067. join 메서드2
print("/".join(interest))

# 068. join 메서드3
print("\n".join(interest))
# \n 제어 문자는 값을 다음 줄에 출력하게 만듦

# 069. 문자열 split 메서드
string = '삼성전자/LG전자/Naver'
interest = string.split('/')
print(interest)

# 070. 리스트 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)
print(data2)
# sorted() 함수는 기본이 오름차순이며, 정렬된 결과는 리스트로 반환
# 내림차순으로 정렬하고 싶을 때는 파라미터 reverse 값을 true로 만들어 주면 됨
# 예시: sorted(range(1,10),reverse=True)


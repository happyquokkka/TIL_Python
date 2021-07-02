# 0702_FRI.py
# 081-100 초보자를 위한 파이썬 문제풀이

# 081. 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 함
# 하지만 'star expression'을 사용하면 변수의 개수가 달라도 데이터 언패킹이 가능
# 튜플에 저장된 데이터 중 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없음
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, star expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, x, y = scores
print(valid_score)

print('-----------------------------------------')

# 082. star expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
x, y, *valid_score = scores
print(valid_score)

print('-----------------------------------------')

# 083. star expression을 사용하여 가운데 8개의 값을 valid_score 변수에 바인딩
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
x, *valid_score, y = scores
print(valid_score)

print('-----------------------------------------')

# 084. temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}

print('-----------------------------------------')

# 085. 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
ice_creams = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(ice_creams)

print('-----------------------------------------')

# 086. 85번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
ice_creams['죠스바'] = 1200
ice_creams['월드콘'] = 1500
print(ice_creams)

print('-----------------------------------------')

# 087. 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print('메로나 가격: %d' % ice['메로나'])

print('-----------------------------------------')

# 088. 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice)

print('-----------------------------------------')

# 089. ★ 다음 딕셔너리에서 메로나를 삭제해라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del ice['메로나']
print(ice)

print('-----------------------------------------')

# 090. 다음 코드에서 에러가 발생한 원인을 설명하라.
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# 에러 발생 원인: icecream 이라는 딕셔너리 안에 '누가바'라는 key는 존재하지 않음.

print('-----------------------------------------')

# 091. 딕셔너리 생성
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory)

print('-----------------------------------------')

# 092. 딕셔너리 인덱싱
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory['메로나'][0],'원')

print('-----------------------------------------')

# 093. 딕셔너리 인덱싱
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory['메로나'][1],'개')

print('-----------------------------------------')

# 094. 딕셔너리 추가
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
inventory['월드콘']=[500,7]
print(inventory)

print('-----------------------------------------')

# 095. ★ 딕셔너리 keys() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
print(ice)

print('-----------------------------------------')

# 096. 딕셔너리 values() 메서드
ice = list(icecream.values())
print(ice)

print('-----------------------------------------')

# ★ 097. 딕셔너리 values() 메서드
print(sum(icecream.values()))
# sum(iterable) -> 파이썬 내장함수
# 리스트나 튜플처럼 인덱스 순환 접근이 가능한 자료형이고, 내부에 숫자로만(정수 or 실수) 이루어져 있어야 함.
# 출처 : https://blockdmask.tistory.com/413

print('-----------------------------------------')

# 098. 딕셔너리 update 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

print('-----------------------------------------')

# ★ 099. zip과 dict
# 아래 두 개의 튜플을 하나의 딕셔너리로 반환
# keys를 키로, vals를 값으로 result라는 이름의 딕셔너리로 저장하라
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
# zip()  -> 내장함수
# 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환
# 출처 : https://horensic.tistory.com/78

print('-----------------------------------------')

# 100. zip과 dict
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price))
print(close_table)
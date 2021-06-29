# 01_slicing.py

# 문자열
# 문자의 나열 - 여러 문자로 이루어져 있기 때뭍에 한 문자당 하나의 메모리 변환
# 'abc' -> a 한칸 b 한칸 c 한칸의 공간을 차지하고 공간이 연속 되어 있음
# ★ 공백도 하나의 문자로 인식 ★

# 인덱싱과 슬라이싱이 가능

# 문자열 생성
crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'

# 특정 인덱스의 문자 출력 - 파이썬의 인덱싱은 0 부터 시작함
print(crawling[0]) # 첫 번째 문자
print(crawling[-1]) # 마지막 문자
print(crawling[2]) # 인덱스 2번 = 3번째 문자

# 슬라이싱 예제
# 변수명[시작인덱스 : stop+1 인덱스]
print(crawling[0:4]) # 0~3번 인덱스까지
print(crawling[5:16]) # 5~15번 인덱스까지
print(crawling[17:]) # stop을 생략하면 끝까지 - 17~ 끝까지
print(crawling[19]) # 인덱스 19번 문자
print(crawling[-1:]) # 시작은 마지막문자에서, 끝까지 - 마지막 문자
print(crawling[-1]) # 위 코드와 같은 결과
print(crawling[:-1]) # 처음부터 마지막 전 문자까지
print(crawling[16:16+4]) # [16:20]과 동일하므로 16~19까지

print("---------------------------------------")

print(parsing)
print(parsing[5:]) # 5번째 문자부터 끝까지 "parsing is also fun"
print(parsing[:15]) # 첫번째 문자부터 14번째까지 "Data parsing is"
print(parsing[:]) # 처음부터 끝까지 "Data parsing is also fun"


print("=========================================")
#### 주의 ####

string = 'happy day!!!'
string_a = string[:5] # 가능!
string[:5] = 'abc' # 문자열의 부분 수정은 불가능
sgring = 'abc12' # 문자열변수 전체 수정은 가능
print(string)

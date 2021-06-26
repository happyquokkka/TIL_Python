# 0626_SAT.py

# 021. 문자열 인덱싱
letters = 'python'
print(letters[0], letters[2])
# 인덱싱 표기는 [순서]

# 022. 문자열 슬라이싱
license_plate = "24가 2210"
print(license_plate[-4:])
# - 기호가 붙으면 끝에서부터 인덱싱 혹은 슬라이싱 함. : 콜론 기호를 붙이면 뒤에서 네 번째부터 인덱싱 끝까지를 의미

# 023. 문자열 인덱싱
string = "홀짝홀짝홀짝"
print(string[::2])
# 슬라이싱 시 시작인덱스:끝인덱스:오프셋을 지정할 수 있음
# 오프셋이란 문자열을 작성할 때 문자마다 매겨지는 고유의 번호를 의미함
# https://soraji.github.io/python/2019/05/22/offsetindex/ 참고한 링크!

# 024. 문자열 슬라이싱
string = 'PYTHON'
print(string[::-1])

# 025. 문자열 치환
phone_num = '010-1111-2222'
phone_num1 = phone_num.replace("-", " ")
print(phone_num1)
# replace 메서드를 사용하면 문자열 일부를 치환할 수 있음
# 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고, 치환된 문자열이 반환됨

# 026. 문자열 다루기
phone_num2 = phone_num1.replace(" ", "")
print(phone_num2)

# 027. 문자열 다루기
url = "http://sharebook.kr"
url_split = url.split('.')   # .을 기준으로 분리
print(url_split[-1])    # 전체 문자열의 마지막에서 첫 번째 문자 표시

# 028. 문자열은 immutable
lang = 'python'
# lang[0] = 'p'
print(lang)
# 예상 결과: python 문자열 전부 출력 될 것 같다
# 가 아니라 문자열은 수정할 수 없어서 대입 연산자를 사용할 수 없다고 한다...

# 029. replace 메서드
string = 'abcdfe2a354a32a'
string1 = string.replace('a','A')
print(string1)

# 030. replace 메서드
string = 'abcd'
string.replace('b', 'B')
print(string)
# aBcd 출력 될 것 같다
# 왜 안됐지???
# 아!! 새로운 변수로 할당하지 않았기 때문...
# string1 = string.replace('b', 'B') 로 입력하고 print(string1)을 하면 aBcd가 될 것 같다
string1 = string.replace('b', 'B')
print(string1)
# 이러면 aBcd가 제대로 출력된다!

print ('-----------------------------------------')

# 031. 문자열 합치기
a = '3'
b = '4'
print(a + b)
# 34로 출력될 것이다

# 032. 문자열 곱하기
print('Hi' * 3)
# 문자열과 정수 곱셈은 같은 형태의 자료가 아니기 때문에 오류가 날 것이다
# 아니다... Hi가 3번 출력되었다

# 033. 문자열 곱하기
print('-' * 80)

# 034. 문자열 곱하기
t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 4)

# 035. 문자열 출력
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print("이름: %s  나이: %d" % (name1, age1))
print('이름: %s  나이: %d' % (name2, age2))
# 두 개 이상의 데이터 타입을 포맷팅 할 경우 괄호 사용하는 것 잊지 말자!!!

# 036. 문자열 출력
print('이름: ' + name1, '나이: ' + format(age1))
print('이름: ' + name2, '나이: ' + format(age2))
# 해설
# print('이름: {} 나이: {}'.format(name1, age1))
# print('이름: {} 나이: {}'.format(name2, age2))

# 037. 문자열 출력
# f-string 사용하기
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

# 038. 컴마 제거하기
num_listedShares = "5,969,782,550"
num_listedShares1 = num_listedShares.replace(",","")
print(int(num_listedShares1))

# 039. 문자열 슬라이싱
term = '2020/03(E) (IFRS연결)'
print(term[0:7])

# 040. strip 메서드
data = "   삼성전자    "
# 문자열에서 strip() 메서드를 사용하면 좌우의 공백을 제거할 수 있음
data1 = data.strip()
print(data1)

print ('-----------------------------------------')

# 041. upper 메서드
ticker = 'btc_krw'
ticker1 = ticker.upper()
print(ticker1)

# 042. lower 메서드
ticker2 = ticker1.lower()
print(ticker2)

# 043. capitalize 메서드
a = 'hello'
b = a.capitalize()
print(b)

# 044. endswith 메서드
file_name = '보고서.xlsx'
a = file_name.endswith('xlsx')
# 이건 확인을 어떻게 할 수 있다는 걸까???
print(a)
# 아하 이것까지 해야 True/ False 값이 나와서 xlsx로 끝나니까 True 값이 출력되는 거였다!
# 출처 : https://homzzang.com/b/py-166

# 045. endswith 메서드
file_name = '보고서.xlsx'
b = file_name.endswith(('xlsx', 'xls'))
print(a)
# xlsx 또는 xls인지를 확인하고 싶으므로 괄호로 두 개를 묶어준다

# 046. startswith 메서드
file_name = '2020_보고서.xlsx'
a = file_name.startswith('2020')
print(a)

# 047. split 메서드
a = 'hello world'
b = a.split()
print(b)

# 048. split 메서드
ticker = "btc_krw"
c = ticker.split('_')
print(c)

# 049. split 메서드
date = '2020-05-01'
d = date.split('-')
print(d)

# 050. strip 메서드
data = '039490       '
d_ = data.strip()
print(d_)


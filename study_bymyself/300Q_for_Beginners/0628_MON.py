# 0628_MON.py
# 1주차 누적복습 _ 분기문(if문)
# Q.121-129

# 121. 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로,
# 대문자일 경우 소문자로 변경해서 출력.
character = input("")
if character.islower() :
    print(character.upper())
else :
    print(character.lower())
# islower(), upper(), lower() 함수들의 사용법: 변수명.islower()
                                            # 변수명.upper()
                                            # 변수명.lower()

# 122. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있을 때 사용자로부터 score를 입력받아 학점을 출력하라.
# 81~100 A
# 61~80 B
# 41~60 C
# 21~40 D
# 0~20 E
score = int(input('score: '))
if score >= 81 :
    print("A")
elif score >= 60 :
    print("B")
elif score >= 41 :
    print("C")
elif score >= 21 :
    print("D")
else :
    print("E")

# 123. 사용자로부터 달러, 엔, 유로 또는 위안 금액을 입력받은 후 원으로 반환하는 프로그램
# 사용자는 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

data = input("입력: ")
tokens = data.split()
amount, currency = tokens
amount = float(amount)

if currency == '달러' :
     print(amount * 1167)
elif currency == '엔' :
    print(amount * 1.096)
elif currency == '유로' :
    print(amount * 1268)
else :
    print(amount * 171)

# 124. 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력
num1 = int(input('input number1 : '))
num2 = int(input('input number2 : '))
num3 = int(input('input number3 : '))
if (num1 > num2) and (num1 > num3) :
    print(num1)
if num2 > num3 :
    print(num2)
else :
    print(num3)

# 125. 사용자로부터 휴대폰 번호를 입력 받고, 통신사를 출력하는 프로그램 작성
num = input('휴대전화 번호 입력: ')
if num.startswith('011') :
    print('당신은 SKT 사용자입니다.')
elif num.startswith('016') :
    print('당신은 KT 사용자입니다.')
elif num.startswith('019') :
    print('당신은 LGU 사용자입니다.')
else :
    print('알수없음')

# 126. 사용자로부터 5자리 우편번호를 입력받고 구를 판별하라.
post_num = input('우편번호: ')
post_num = post_num[:3]  # 입력받은 우편번호 중 앞의 세 자리만 필요하므로 다시 바인딩한다
if post_num in ['010', '011', '012'] :
    print('강북구')
elif post_num in ['014', '015', '016'] :
    print('도봉구')
else :
    print('노원구')

# 127. 사용자로부터 13자리의 주민등록번호를 입력받은 후 성별(남/여)을 출력하는 프로그램 작성
resident_number = input('주민등록번호(-를 포함하여 입력하시오) : ')
resident_number = resident_number.split("-")    # ['111111', '1234567']
if resident_number[0] == "1" or resident_number[0] == "3" :
    print('남자')
else :
    print('여자')

# 128. 주민등록번호의 뒷 자리 7자리 중 두 번째와 세 번재는 지역코드를 의미한다
# 주민등록번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
resident_number = input('주민등록번호(-를 포함하여 작성하시오): ')
back = resident_number.split("-")[1]   # ['111111', '12345667'] 중 '1234567'
if 0 <= int(back[1:3]) <= 8 :   # 주민등록번호 뒷 7자리의 두번째부터 세번째가 0이상 8이하 일때
    print('서울입니다.')
else :
    print('서울이 아닙니다.')

# 129. 주민등록번호 중 마지막 자리수는 주민등록번호의 유효성 체크에 사용됨
# 먼저 앞에서부터의 12자리숫자에 2, 3, 4, 5, 6, 7, 8,  9, 2, 3, 4, 5를 차례로 곱한 뒤
# 그 값을 전부 더한다.
# 연산 결과 값을 11로 나누면 나머지가 나오는데, 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다
resident_number = input('주민등록번호(-를 포함하여 작성하시오): ')
front = (resident_number.split("-")[0])
back = resident_number.split("-")[1]

cal1 = (int(front[0]) * 2) + (int(front[0]) * 3) + (int(front[0]) * 4) + (int(front[0]) * 5) + (int(front[0]) * 6) + \
       (int(front[0]) * 7) + (int(front[0]) * 8) + (int(front[0]) * 9) + (int(front[0]) * 2) + (int(front[0]) * 3) + \
       (int(front[0]) * 4) + (int(front[0]) * 5)
cal2 = 11 - (cal1 % 11)

if str(cal2) == back[6] :
    print('유효한 주민등록번호입니다.')
else :
    print('유효하지 않은 주민등록번호입니다.')


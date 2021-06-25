# 011. 변수 사용하기
samsungelectronics = 50000
total = samsungelectronics * 10
print(total)

# 012. 변수 사용하기
total_price = 2980000000000
now_price = 50000
PER = 15.79
print(total_price)
print(now_price)
print(PER)

# 013. 문자열 출력
s = "hello"
t = "python"
print(s + "! " + t)

# 014. 파이썬을 이용한 값 계산
# 코드의 실행 결과 = 8
print(2+2*3)

# 015. type 함수
a = "132"
# a는 문자열(str)의 형태로 바인드 되어있다
print(type(a))

# 016. 문자열을 정수로 변환
num_str = "720"
num_str = int(num_str)
print(type(num_str))

#  017. 정수를 문자열 100으로 변환
num = 100
num = str(num)
print(type(str))

# 018. 문자열을 실수로 변환
num = float("15.79")
print(type(num))

# 019. 문자열을 정수로 변환
year = "2020"
n_year = int(year)
print(n_year, n_year-1, n_year-2)

# 020. 파이썬 계산
# 에어컨이 월 48,584원에 무이자 36개월의 조건으로 판매되고 있음
# 총 금액을 계산한 후 화면 출력

month_price = 48584
total = 48584 * 36
print(format(total, ','),"원")

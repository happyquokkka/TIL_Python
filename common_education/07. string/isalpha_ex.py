# isalpha_ex.py

# 그림과 같이 문장을 입력하고
# 알파벳, 숫자, 스페이스, 기타 개수 출력
# 개수 세는 건 무조건 누적합이라고 외워라 좀 외워

sentence = input('문장을 입력하세요: ')

c = 0   # 문자 누적 변수
d = 0   # 숫자 누적 변수
s = 0   # 스페이스 누적 변수
o = 0   # 기타 누적 변수

for i in sentence :
    if i.isalpha() :
        c += 1
    elif i.isdigit() :
        d += 1
    elif i.isspace() :
        s += 1
    else :
        o += 1
print('알파벳: %d개' % c)
print('숫자: %d개' % d)
print('스페이스: %d개' % s)
print('기타: %d개' % o)


# print('알파벳 :', sentence.isalpha())
# print('숫자 :', sentence.isdigit())
# print('스페이스 :', sentence.isspace())
# print('기타 :', sentence.isalnum())
# 05_find_index_ex1.py

# 이메일 주소를 입력 받아서, 이메일 형식이 아니면 "이메일 형식이 아닙니다." 출력
# 이메일 형식이 아닌 경우는 다음과 같음
# @가 없는 경우
# . 없는 경우
# @과 . 위치가 바뀐 경우
# @과 . 사이에 문자가 없는 경우
# @ 앞에 문자가 없는 경우
# . 뒤에 문자가 없는 경우
# @ 가 두 번 이상 있는 경우
# . 가 두 번 이상 있는 경우

# 올바른 이메일 형식 : 아이디(문자로만 구성)@사이트명.도메인
# 문자열 인덱스 번호 : 0, 1, 2, 3 ... 뒤로 갈 수록 커진다
# 그니까 @ 가 . 뒤에 있는 경우에는 @의 인덱스가 . 의 인덱스보다 크다
# . 가 @ 앞에 있는 경우에는 .의 인덱스가 @의 인덱스보다 작다

email = input('이메일 입력 : ')

at = 0  # @ 누적 변수
dot = 0  # . 누적 변수

# @ 나 . 가 없는 경우
if {(email.find('@')) == -1} or {(email.find('.')) == -1} :
    print('첫 번째 이메일 형식이 아닙니다.')

# @ 와 . 위치가 바뀐 경우 -> @ 가 . 뒤에 있거나, . 가 @ 앞에 있는 경우
# @와 . 의 int(index(email))을 비교
elif {(int(email.find('@')) > (int(email.find('.')) ))} or {(int(email.find('.'))) > (int(email.find('@')))} :
    print('두 번째 이메일 형식이 아닙니다.')

# @ 앞에 문자가 없는 경우
elif not email.split('@')[0].isalpha() :
    print('세 번쨔 이메일 형식이 아닙니다.')

# . 뒤에 문자가 없는 경우
elif not email.split('.')[1].isalpha() :
    print('네 번째 이메일 형식이 아닙니다.')

# elif @ 와 . 사이에 문자가 없는 경우
elif not (email.split('@')[1].isalpha()) and (email.split('.')[0].isalpha()) :
    print('다섯 번째 이메일 형식이 아닙니다.')

# @ 나 . 가 두 번 이상 있는 경우
for n in email :
    if n.find('@') :
        at += 1
    elif n.find('.') :
        dot += 1
    elif (at >= 2) or (dot >= 2) :
        print('여섯 번째 이메일 형식이 아닙니다.')

else :
    print('이메일 형식이 맞습니다.')

print('입력한 이메일: %s' % email)


# 왜 올바른 형식도 올바르지 않다고 뜰까...?

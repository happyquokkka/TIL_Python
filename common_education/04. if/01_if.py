# 01_if.py

# password = 1234
password = 12345
# if password == 1234 :
#     print("비밀번호가 일치합니다")  # if문 내부
#
# print("끝")  # if문 종료 후 실행

if password == 1234 :
    print("비밀번호가 일치합니다 - if문 내부")  # if문 내부
else :
    print("비밀번호가 일치하지 않습니다 - else문 내부")

print("끝 - if ~ else 문 밖입니다")

# 들여쓰기 : 탭키 / 스페이스키 4칸

# else문이나 if 문에서 아무것도 수행하지 않게 하려면

if password == 1234 :
    print("비밀번호가 일치합니다 - if문 내부")  # if문 내부
else :
    pass # 아무것도 수행하지 않고 문장들 종료
         # else를 집어넣어야 되는데 아무 것도 수행하면 안 될 때 pass 명령문 사용

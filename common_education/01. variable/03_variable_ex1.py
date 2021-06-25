name = "홍길동"
no = "2016001"
year = "4"
grade = "A"
average = "93.5"

print("성명 :", name)
print("학번 :", no)
print("학년 :", year)
print("학점 :", grade)
print("평균 :", average)

#더하기로 연결할지, 콤마로 연결할지는 개발자의 선택


## 포맷코드 사용해보기

name = '홍길동'
no = '2016001'
year = 4
grade = 'A'
average = 93.5
level = 10

# 문자열 : %s
# 문자 1개 : %c
# 정수 : %d
# 실수 : %f

print("성명 : %s" % name)
print("학번 : %s" % no)
print("학년 : %d" % year)
print("학점 : %c" % grade)
print("평균 : %.2f" % average)
print("등급 : %d %%" % level)   #등급 : 10% - %문자를 출력할 때는 %%

# 05_file_readline.py

# 파일 읽기 방법
# readline()
# 1개 행씩 읽어 오기
# 1행 끝에 ‘\n’ 포함

# readlines() :
# 모든 행을 읽어 라인 별로 잘라서 리스트 생성
# 1개 행이 1개 요소
# [‘..’, ‘…’, ‘…’, …, ‘…’]

# read()
# 내용 전체를 읽어서 문자열로 반환

print('--- 첫 번째 행 읽기 ---')

f1 = open('test.txt','r') # ansi 형태의 파일
# 읽어 올 데이터를 받아서 쓸 변수 지정 -> 파일을 핸들링하려면 반드시 변수 설정 필요
line = f1.readline()  # 첫 번째 라인 1개 읽어오기
print(line) # 안녕하세요, 홍길동입니다. ㅡ 한글 깨지지 않고 제대로 출력
f1.close()

# readline() 함수를 이용해서 전체 라인 읽어오기
# 1행씩 읽고 출력을 반복 ㅡ 더 이상 파일의 내용이 없을 때까지 반복

# print('--- 파일 전체 읽기 ---')
#
# f2 = open('test.txt', 'r')

# while True :  # 무한반복 (몇 행인지 알 수 없음)
#     line = f2.readline()    # 라인 1개 읽고
#     # readline() 함수는 포인터를 자동으로 밑으로 내려 읽기를 진행함
#     if not line :  # 읽을 내용이 없으면
#         break      # 반복문 종료
#     print(line, end='')    # 출력 후 다음 반복 실행
# f2.close()

# 파일 전체라인을 읽어와서 다른 파일에 쓰는 코드
# 2개의 파일 객체 필요
f2 = open('test.txt', 'r')  # 원본 : 읽어올 파일 객체
f3 = open('test_write.txt','a', encoding='utf-8')

while True :  # 무한반복 (몇 행인지 알 수 없음)
    line = f2.readline()    # 라인 1개 읽고
    # readline() 함수는 포인터를 자동으로 밑으로 내려 읽기를 진행함
    if not line :  # 읽을 내용이 없으면
        break      # 반복문 종료
    f3.write(line)
    print(line, end='')    # 출력 후 다음 반복 실행
f2.close()
# list_append_ex1.py

# 3명의 회원을 입력 받아 리스트에 추가하고, 리스트 내용 출력 (for문 사용)
names = []
for name in range(0,5) :
    new = input('회원 입력: ')
    names.append(new)
print('회원 명단: ', names)
# 09_file_append.py
# append : 파일 끝에 추가하는 기능
# 파일 열기 모드 : a

f = open('test2.txt','a')

append_data = '\n\nPython programming'
f.write(append_data)

#
f = open('test2.txt','r', encoding='utf-8')
# 에러 생기면 그 다음에 encoding 명령 추가하면 됨
print(f.read())

f.close()

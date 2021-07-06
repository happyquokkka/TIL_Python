# 01_file_create.py

# 파일생성 : 파일명만 적으면 현재 디렉터리에 생성해 줌
# 파일객체변수명 = open(파일명, 모드"w")
# 위코드 실행 후 파일 핸들링 위해서는 파일객체변수명을 사용함
# 경로 설정이 매우 중요함!!!! 꼭 기억!!!

f=open('file1.txt','w')
# fil1.txt 파일이 현재 폴더에 없으면 새 파일 생성, 있으면 해당 파일의 내용을 지우고 열어줌
f.close()

# 파일을 쓰기 모드(w)로 연다
# 해당 파일이 존재하지 않으면 새로 생성하고
# 존재하면 덮어 씀 (기존 내용 없어짐)

# 현재 폴더 외 다른 폴더에 저장하고 싶으면 전체 경로를 적으면 됨
f = open('../file2.txt','w')
# ../ 의 의미는 현재 폴더보다 하나 위 폴더(상위) = 현재 위치보다 하나 위는 ch03
f.close()

f = open('c:/file1.txt','w')    # 파이썬에서 경로(디렉터리)표시는 / 를 이용
# 역슬러시를 이용하면 에러 발생함
f.close()

# c드라이브 아래 PythonStudy 폴더에 file_test.txt 파일을 생성
f = open('c:/PythonStudy/file_test.txt','w')  # 절대경로 - 최상위 디렉터리 기준(윈도우 c:/)
f.close()

f = open('../../PythonStudy/file_test.txt','w')  # 상대경로 - 현재 위치 기준
f.close()

# 경로에 표시된 디렉터리명이 실제 없으면 에러 발생
f = open('../abc/test.txt','w')
# 상대경로 ㅡ 현재 폴더의 상위폴더에서 abc 이름의 폴더를 찾고 그 안에 test.txt 생성
# FileNotFoundError: [Errno 2] No such file or directory '../abc/test.txt'
f. close()
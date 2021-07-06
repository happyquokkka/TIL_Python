# 08_file_search.py
# 파일 내에서 검색 예제
# 사실상 파일을 읽어오면 문자열 형태로 저장되기 때문에 문자열 내에서 검색
# read() 함수 이용하여 파일 내용을 문자열로 저장

f = open('test2.txt','r', encoding = 'utf-8')
# cp949 에러 발생 시 encoding이 있었으면 지워보고, 없었으면 넣어보기
data = f.read()     # test2.txt 파일 내용을 문자열로 data 변수에 저장

# 검색값 입력
value = input('검색 값 입력: ')

# 문자열에 검색 값이 있는지 확인
if value in data :
    print('있음')
else :
    print('없음')

f.close()

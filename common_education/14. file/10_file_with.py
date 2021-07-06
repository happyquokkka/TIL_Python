# 10_file_with.py
# with() : 문장이 끝나면 자동으로 파일을 닫아주는(close)기능
# 가독성이 높아짐

with open('test3.txt','w') as f :
    f.write('hello')

file = 'test4.txt'
data = '''Python programming
R programming
web programming'''

with open(file,'w') as f :
    f.write(data)

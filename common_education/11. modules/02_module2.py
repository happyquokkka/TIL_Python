# 02_module2.py

# from 디렉토리명 import 함수명
from module import a        # a 모듈명만 import ㅡ a.함수명()
from module import b        # b 모듈명만 import ㅡ b.함수명()
from module.b import *      # 모든 함수까지 import ㅡ 함수명()

a.hello('홍길동')
b.hello_1()
hello_1()


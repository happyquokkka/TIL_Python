# 01_module1.py

# 실행 코드

# 생성한 모듈 new_calculator import
import new_calculator           # 모듈파일 명에 대해서만 얘기를 했기 때문에
from new_calculator import sub  # new_calculator 모듈에서 sub 함수를 import (특정 함수만)
from new_calculator import *    # 모듈 안에 있는 모든 함수import


a = new_calculator.add(7,4)
print(a)

# sub 함수를 import 했으므로
# 앞에 모듈명을 적지 않고 함수명만 적어서 사용 가능
s = sub(7,4)
print(s)

m = mul(7,4)
print(m)

print(div(7,4))

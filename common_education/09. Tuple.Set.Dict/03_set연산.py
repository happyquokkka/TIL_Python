# 03_set연산.py
# 연산자로 연산을 하는 게 함수보다 빠르게 처리되기는 한다
# 그렇지만 개발자 본인이 편리한 방법을 쓰면 된다

A = {1,2,3}
B = {3,4,5,6}

# 합집합 -
# a|b (역슬러시키 + shift)
print(A|B)
# a.union(b)
print(A.union(B))

print('---------------------')

# 교집합
# a & b
print(A&B)
# a.intersection(b)
print(A.intersection(B))

print('---------------------')

# 차집합
# a - b
print(A-B)
# a.difference(b)
print(A.difference(B))
# 02_list_indexing.py
# 특정 원소에 접근 = 인덱싱
# 리스트에서 인덱스 연산자를 통하여 요소를 참조(접근)하는 것

a = [1,2,3,4,5]
a[0] # 리스트의 첫 번재 요소 (1)
a[-1] # 리스트의 마지막 요소 (5)
a[-2] # 뒤에서 두 번째 요소 (4)

b = [1,2,3,[10,20]]
b[-1]  # [10,20] 반환
b[-1][0]  # 10 반환

c=[1,3,[5,6],8]

# 원소값 6을 접근해서 출력하시오.
print(c[2][1])

d = [1,2,3,[4,5,[7,8]],2]

# 8을 접근해서 출력하시오.
print(d[3][2][1])

print('-------------------')

a = [1,2,3,4,5]
b = [1,2,3,[10,20]]
c = [1,2,3,[10,20],4,5]
all_list = [a,b,c]

print(all_list) # [[1, 2, 3, 4, 5], [1, 2, 3, [10, 20]], [1, 2, 3, [10, 20], 4, 5]]

all_list[-1][3][0]
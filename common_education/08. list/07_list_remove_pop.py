# 07_list_remove_pop.py

n = [1,2,3,3,4,5,4,3]
n.remove(4)     # 첫 번째로 존재하는 4만 제거하고 원본에도 반영됨
print(n)        # [1, 2, 3, 3, 5, 4, 3]

print('----------------------------')

# n 리스트에서 원소값이 3인 원소를 모두 제거하시오.
# 3의 개수를 확인해야 함
count = n.count(3)  # ㄷ개 들어 있음
print(count)

for i in range(count) :
    n.remove(3)
    print('3 삭제', n)

print(n)

print('----------------------------')

n1 = [1,1,2,1]
n1.remove(1)  # 요소 값이 없는데 remove 함수를 사용하면 에러 발생
# 제거하기 전에 반드시 요소가 있는지 확인!!!

# pop() : 리스트 마지막 요소 반환하고 삭제
x = ['a','b','c','d']
y = x.pop()     # 'd'
print(y)    # 반환된 마지막 요소 = d
print(x)    # d 삭제된 나머지 요소만 확인 ['a', 'b', 'c']

# x에 남아 있는 요소 3개를 pop
# 계속 pop 실행해서 더 이상 요소가 없으면 빈 리스트로 남게 됨
x.pop()  # ['a', 'b']
x.pop()  # ['a']
x.pop()  # []
print(x)  # [] / 리스트인 변수는 유지하나 빈 리스트로 반환

# x가 빈 리스트인 경우 에러 발생
# x.pop() # IndexError: pop from empty list 오류 발생

# pop(인덱스) : 인덱스 위치에 있는 요소 반환하고 삭제
heroes = ['슈퍼맨', '스파이더맨', '헐크', '아이언맨', '배트맨']
tmp = heroes.pop(2)  # 세번째 : 헐크 삭제
print('삭제된 값 :', tmp)
print('삭제 후 리스트',heroes)

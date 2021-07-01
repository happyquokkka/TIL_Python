# 04.집합예제.py

# 파티에 참석한 사람이 다음과 같을 때 집합 생성하고 그림과 같이 출력
# partyA : "Park", "Kim", "Lee"
# partyB : "Park", “길동“, “몽룡”

# 집합 생성
partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}

# 파티에 참석한 모든 사람
print('파티에 참석한 모든 사람 :', partyA.union(partyB))
    # 중복되는 데이터는 한 번만 나타남
# 2개의 파티에 참석한 모든 사람
print('2개의 파티에 참석한 모든 사람 :', partyA.intersection(partyB))
# 파티 A에만 참석한 사람
print('파티A에만 참석한 사람 :', partyA.difference(partyB))
# 파티 B에만 참석한 사람
print('파티B에만 참석한 사람 :', partyB.difference(partyA))

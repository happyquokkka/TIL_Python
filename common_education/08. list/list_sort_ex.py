# list_sort_ex.py

# append() 연습문제2를 복사
# 점수를 내림차순 정렬하여 출력

good = 0
scores = []
student = int(input('학생 수 입력 : '))
for i in range(1,student+1) :
    score = int(input('학생%s 점수 입력 : ' % i))
    scores.append(score)
    if score >= 80:
        good += 1

total = sum(scores)
avg = total/len(scores)

print('총점: %d' % total)
print('평균: %.2f' % avg)
print('80점 이상 학생 : %d명' % good)
scores.sort(reverse=True)
print('점수 내림차순 정렬 :', scores)



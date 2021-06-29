# while_ex1.py

# 노래방 기계 : 1곡에 2000원
# 현재 잔액 : 10,000원

money = 10000
song = 2000
n = 0

while money > 0 :
    n += 1
    print('노래를 %d곡 불렀습니다' % n)
    print('현재 %d원 남았습니다.' % (money-(song*n)))
    if n == 5 :
        print('노래를 %d곡 불렀습니다' % n)
        print('잔액이 없습니다. 종료합니다.')
        break


# 선생님 풀이

song = 2000
money = 10000
count = 0 # 몇곡을 불렀는지 누적하는 변수

while money != 0 : # money가 0이 아닐 때 반복
    count += 1
    money = money - song
    print('노래를 '+str(count)+ '곡 불렀습니다.')

    if money == 0 : # money가 0이면
        print('잔액이 없습니다. 종료합니다.')
        break
    else :
        print('현재 '+str(money)+'원 남았습니다.')

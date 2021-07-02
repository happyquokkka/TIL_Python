# function_gbb_game.py

# 함수명 : gbb_game()
# 랜덤으로 COM 숫자를 생성해서
# 전달받은 YOU 숫자와 비교하여
# 결과 출력

from random import *

# 랜덤 정수 생성
def gbb_game() :
    global com
    com = randint(1,3)

# YOU 숫자 전달 받기
def gbb_game1() :
    global you
    you = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))

# YOU 숫자와 COM 숫자 비교
def gbb_game2() :
    if (you == 1 and com == 3) or (you == 2 and com == 1) or (you == 3 and com == 2):
        print('당신이 이겼습니다')
    elif you == com :
        print('비겼습니다')
    else:
        print('컴퓨터가 이겼습니다')
    print('COM :',com)

gbb_game1()
gbb_game()
gbb_game2()

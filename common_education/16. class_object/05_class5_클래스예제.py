# 05_class5_클래스예제.py

# 1. 숫자를 하나 증가하는 메서드
# 2. 숫자를 0으로 초기화하는 메서드
# 3. 숫자를 저장하는 속성(멤버변수) ㅡ 생성자 함수에서 만들기
# 4. 현재 숫자값을 출력하는 메서드

class Counter :
    def __init__(self):
        self.num = 0

    def increment(self):
        self.num += 1

    def reset(self):
        self.num = 0    # 숫자를 0으로 초기화하는 메서드

    def print_current_value(self):
        print('현재 저장되어 있는 숫자값은 : ', self.num)


# 객체 생성
c1 = Counter()
c2 = Counter()
c3 = Counter()

# 질문: c1 인스턴스와 c2 인스턴스는 공통의 멤버변수 num을 사용한다. (X)
#      변수의 이름은 같으나 메모리 공간 자체가 다르게 만들어짐.

c1.increment()
c2.increment()
c1.increment()
c2.increment()
c1.increment()
c2.reset()
c1.print_current_value()
print(c1.num)
c2.print_current_value()
print(c2.num)
print(c3.num)




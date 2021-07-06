# 08_class_super.py

# super/부모/base 클래스
class person :
    # 생성자 함수
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def eat(self, food) :
        print('{}은 {}를 먹습니다.'.format(self.name, food))

    def sleep(self, minute) :
        print('{}은 {}분 동안 잡니다'.format(self.name,minute))

    def work(self, minute) :
        print('{}은 {}분 동안 일합니다'.format(self.name,minute))

# 상속 : class 클래스명(부모클래스명)

# child 클래스 생성(Student, Employee)
class Student(person) :   # student 클래스는 person이라는 클래스를 상속받는다
    def __init__(self,name,age):    # 생성자 함수 따로 만들기
        self.name = name
        self.age = age

# 하위 클래스에서 부모 큻래스가 갖고 있는 함수(메서드)를 재정의 하는 것 = 메서드 오버라이드(method override)
# 하위 클래스(자식 클래스)에서 부모클래스의 method를 호출할 때 사용 ㅡ super()

    def work(self, minute) :
        super().work(minute)  # 부모 클래스(super())의 메서드 work 을 호출해서 실행
        print('{}은 {}분 동안 강의를 듣습니다'.format(self.name, minute))

class Employee(person) :
    def __init__(self,name,age):    # 생성자 함수 따로 만들기
        self.name = name
        self.age = age

bob = Employee('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)

lee = Student('Lee',19)
lee.eat('NOODLE')
lee.sleep(60)
lee.work(30)    # 부모클래스의 work() 메서드와 하위 클래스의 work() 메서드가 같이 호출되게 됨

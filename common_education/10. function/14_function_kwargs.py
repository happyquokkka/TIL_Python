# 14_function_kwargs.py

# 가변길이 매개변수 **kwargs
# keyword arguments의 약자, key=value 형태로 값을 받는다

def show_keywords(**kwargs) :   # 전달받을 때 인수가 dict 형태로 전달됨
    print(kwargs)
    print(type(kwargs))

# 함수 호출
show_keywords()     # 빈 딕셔너리가 전달된다
show_keywords(a=3)
show_keywords(id='sun',
              name='kim',
              phone='010-1234-1234')

show_keywords(num=3,
              val='kim',
              str='abcdef')

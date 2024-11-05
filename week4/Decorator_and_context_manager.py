
# 데코레이터란 힘수또는 메서드를 꾸며주어서 추가적인 기능을 하게 해줌
# 원래 함수를 함수로 덮어 새로운 기능을 넣는다.

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):

        print("추가 기능 실행 전")
        result = original_function(*args, **kwargs)
        print("추가 기능 실행 후")
        return result
    
    return wrapper_function


def display():
    print("원래 함수")

# print(display())

@decorator_function
def display():
    print("원래함수")

print(display())
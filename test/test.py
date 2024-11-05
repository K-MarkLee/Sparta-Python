def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"실행 전: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"실행 후: {func.__name__}")
        return result
    return wrapper

@log_decorator
def say_hello(name):
    print(f"안녕하세요, {name}님!")

# 함수 호출
say_hello("Alice")

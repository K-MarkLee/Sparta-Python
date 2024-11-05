# 변수는 이름과 내용을 넣으면 된다.
name = "승열"

# 변수 선언하기 a는 변수 10은 할당 값
a = 10
b = 12

# 변수를 할당하기 sayhi 는 변수 "Hello, "는 할당 값
sayhi = "Hello, "+ name


# 같은 변수에 할당값 갱신하기
name = "승열"
name = "마크"

# 변수 이름 규칙
# if, for, class 와 같은 파이썬 할당 언어는 변수 이름으로 할 수 없음

# a와 A는 다른 변수로 인식
a = 10
A = 11

# 문자와 숫자 그리고 밑줄만 사용 가능

# 변수의 시작은 숫자로 불가능

# 이름은 알기 쉽게 명확하게 하기
a = 10
num1 = 10

# 동시에 값 할당하기
num1, num2, num3 = 1,2,3

# 같은 값 할당하기
num1 = num2 = num3 = 100

# 변수 활용하기
# input은 값을 직접 넣어야 한다는뜻
name = input("이름을 입력해주세요")
sayhi = "Hello, "+name
print(sayhi)
# f는 변수또한 실행이 가능하게 해준다
print(f"Hello, {name}")

# 변수와 메모리
def greet():
    message = "Hello, "+name
    print(message)

greet()
# greet()안의 message변수는 def 함수 안에서만 사용 가능.
# print(message) 에러발생

# 이때 message는 지역 변수(local variable)이고, 만약
message = "Hello, 승열"
# 이라면 전역 변수(global variable) 라고 할 수 있다.






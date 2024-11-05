# def는 함수를 만들기 위한 지정어

def myfunction(first_number, second_number):
    first_number %= 2
    second_number %= 3
    print(first_number + second_number)
    return True
# return 은 myfunction 에 true값을 집어 넣는것. 표시되지 않아도 할당이 되어 있기에,
# a = myfunction(9,8)한 뒤에, print(a)를 하면 True가 출력됨.


myfunction(9, 8)


# 이름을 넣으면 인사하기
def sayhi(name):
    return print(f"안녕하세요, {name}님!")


username = str(input("이름을 알려주세요! : "))
sayhi(username)


# 매개변수
# 매개변수란, 함수가 호출될 때 입력받는 값을 처리하기 위한 변수이다.
# 위의 sayhi의 함수에 name은 매개변수 이고, username은 인수이다.
# 즉 매개변수는 함수에 변수값을 넣으라고 하는 가이드 이고, 인수는 그 가이드를 보고 호출하는 유저의 인풋값이다.

# return 은 함수를 돌려서 생성되는 반환값이다.
# 복수 반환값은 함수에서 반환값이 여러개 있는 함수를 뜻한다.

def sayhi(name, age):

    print(f"안녕하세요, {name}님!")

    if age < 20:
        print(f"{name}님, {age}살 이시네요! 젊으시네요!")
    elif age > 20:
        print(f"{name}님, {age}살 이시네요! 성인이시군요!")
    else:
        print("나이를 정확하게 입력해 주세요!")
    return name, age


username = str(input("이름을 알려주세요! : "))
userage = int(input("나이를 입력해주세요!(숫자만) : "))
sayhi(username, userage)

# 반환값이 2개인 함수의 예시이다.


# 반환값이 없는 함수

def test_function():
    print("hello")

a = test_function()
print(a)

# a 를 실행하면 프린트는 되지만 이는 휘발성으로 값이 저장되지는 않는데
# 따라서 a에는 아무런 값이 저장이 되지 않기 때문에 이는 반환값이 없는 함수이고,
# 위의 sayhi의 경우에는 만약 sayhi만 불러오게됬을때, name과 age가 반환값으로 정해져 있기 때문에 name과 age가 나올 것이다.


# 기본값이란, 매개변수에 값을 입력 하지 않았을때, 기본적으로 값을 나타내 줄 수 있게 해주는 방법이다.

def sayhi(name = "승열", age = 26):
    print(f"안녕하세요, {name}님 {age}살이군요!")

username = str(input("이름을 알려주세요! : "))
userage = int(input("나이를 입력해주세요!(숫자만) : "))
sayhi(username, userage)

# 이렇게 매개변수에 기본값을 넣게 되면 sayhi()를 실행했을때, 오류가 뜨기 보다는 기본값 즉 "안녕하세요, 승열님 26살이기군요!" 가 표시 될 것이다.
# 중요한 점은 만약 name에만 또는 age에만 기본값을 뒀을때, 아무것도 안넣고 함수를 불러오면 에러가 뜨며, sayhi()에 인수를 한개만 넣을때, 
# 인수의 순서는 기본값을 넣지 않은 매개변수에 먼저 들어가게됨으로, 만약 다중으로 기본값이 들어가게 되었을 때, 주의해야 한다.



# 가변 매개변수
# 가변 매개변수는 정해지지 않는 갯수의 인수를 받을 수 있도록 한다.
# 즉 sayhi에서는 이름과 나이 1개씩만을 받을 수 있지만, 가변 매개변수에서는 여러개 입력이 가능하다.

# 이 때, args 와 kwargs를 사용하게 되는데, args는 리스트를 kwargs는 딕셔너리 형식이라고 보면 된다. 이때 저장은 튜플 tuple형식으로 저장된다.

def numbers (**args):
    print(args)
    return True

numbers(1,2,3,4,5)
# >> (1,2,3,4,5)


def person(**kwargs):
    print(kwargs)
    return True

person(name = "이승열", age = 26)
# kwargs로 이름인 이승열 과 나이인 26을 가져가는 모습을 보여준다.

# args 와 kwargs를 같이 쓸 수도 있다.

def test(num1, num2, *args, **kwargs) :
    print(num1, num2, args, kwargs)
    return True

test(1,2,1,2,name="test", age=1)
# >> 1 2 (1, 2) {'name': 'test', 'age': 1}
# 이는 num1과 num2는 1자리의 숫자를, args리스트를 그리고 kwargs는 딕셔너리 형식으로 받기에, 그에 맞춰서 들어가는 걸 볼 수 있다.
# 만약 데이터 값을 맞춰서 넣지 못하면 에러가 발생하게 된다.


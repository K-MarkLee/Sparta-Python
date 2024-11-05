
class Ai_student:
    def __init__(self,inputname):
        self.name = inputname

    def greet (self):
        print("Hello my name is", self.name)

    def test (a):
        print("This is test")
# 클래스 안의 함수에서 self는 관례이지만 ()안에 어떤 문자가 들어가도 실행은된다(self의 의미를 가짐)
# 하지만 비워 둘 경우 에러가 뜬다.

alice = Ai_student("Alice")
bob = Ai_student("Bob")
alice.greet()
bob.greet()
alice.test()


# pass를 넣는다면, 코드를 적는중 이 함수는 패스하고 다음 코드로 넘어가 테스트 하기 편하게 해준다.

# 매직 메서드란, 미리 정의된 메서드 이다. 예시로는 __init__이 있다.
# 매직 메서드란 내부적인 메서드 이기도 하다.
# 메서드란 클래스 안에 있는 함수이다.
# 매직 메서드는 객체와의 연결성이 좋기 때문에 가장 자주 쓰이고 중복이 될거 같은 것에 설정을 하면 좋을 것 같다.
class human:

# __init__은  객체가 생성이 될때, 자동으로 호출이 되며, 객체의 초기화를 담당한다.
    def __init__(self, name, age):
        self.name = name
        self.age = age

# __repr_은 print와 같이 표시를 해주는 함수이지만, print와는 달리 공식적인 내용을 뽑아와준다.
# 이는 __repr__목적 같은것이고 사실상 표시만 하려고 한다면 print또는 다른 함수를 써도 되지만,
# 내부함수가 있음에도 사용자 함수를 만들어 쓰는 것 처럼 이또한 디폴트 적인 함수 중 하나이다.
    def __repr__(self):
        return f"human ('{self.name}', {self.age})"


# 객체 간의 뎃셈을 연산해준다. 따로 함수를 불러오지 않고 + 연산자로 호출 할 수 있다.
    def __add__(self, other):
        print(self.name+other.name)
        print(self.age+other.age)


# 객체 간의 비교를 해준다. 이또한 따로 함수를 불러오지 않고 연산자 즉 == 로 호출 할 수 있다.
    def __eq__(self, other) :
        if self.name == other.name :
            print("이름이 같습니다")
        else :
            print("이름이 다릅니다")


# 이 메서드 에서는 한번에 하나의 반환값만 도출 하기 때문에, 만약 이름만 불러 온다거나, 나이만 불러온다거나 등 불가능하다.
    def __str__(self):
        return f"{self.name}님은 {self.age}살입니다."


mark = human('이승열',26)
dark = human('어승열', 26)
print(repr(mark))

mark+mark
mark == dark
print(mark.name)


# 클래스 메서드

class MyClass:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        

# 클래스 변수이다. 이는 클래스 내부 뿐만이 아닌, 이 클래스에 생성된 모든 개체에서도 공유를 한다.
# 즉 클래스 안에서 변수를 변경해버리면, 변경값이 모든 클래스에 전달되므로 주의해서 사용해야 한다.
    class_variable = 0

# 클래스 메서드 를 정의하는 방법이다.
    @classmethod

    def increment(cls):
        cls.class_variable += 1

# 받는 매게변수를 cls로 변경, 아래의cls.class_variable 의 코드를 실행
    def increments(cls, user):
        user.age += 1


# 원래 메서드를 불러 올때는, 메서드의 이름 을 불러와야 하는것 이지만, 여기에서는 변수를 불러왓다.
MyClass.increment()
print(MyClass.class_variable)
myage = MyClass("mark", 26)

# for i in range(0, 11, 1):
#     MyClass.increments()
#     print(MyClass.class_variable)


# 정적 메서드의 예시
class Utility:

# 정적 메서드란 클래스와객체는 없이 맥락에서만 의미가 있다.
# 따로 self나 cls를 안불러 와도 된다.
    @staticmethod
    def add(x,y):
        return x+y
    
print(Utility.add(1,2))

# 상속
# 상속이란 부모가 되는 클래스의 함수 및 내용을 물려 받아서 재사용하는 개념이다.

class Animal:
    def __init__(self,name):
        self.name = name

    def speak (slef):
        return "소리를 냅니다"


# 클래스명 에서 ()는 부모의 클래스 이다.
class Dog(Animal):

# 상속을 받아도 그것을 재정의 할 수 있다.
# 이를 메서드 오버라이딩 이라고 한다
    def speak(self):
        return f"{self.name}가 멍멍 짖습니다."
    

dog = Dog("Mickey")
# Dog 클래스 에는 이름을 불러오는 메서드가 없는데도, 부모에 있기 때문에 들어가는것을 알 수 있다.
print(dog.speak())


# 만약 부모에는 없지만 자식 클래스에서 새로운 인수를 원할때는 
# dog클레스에서 , init을 불러와준다.

class Dog(Animal):
    def __init__(self, name, age) :

# 이것은 자식 클래스에서 받은 이름을 재정의 하기 위해 필요한것
# 이렇게 되면 자식 클래스에서도 이름이 자동으로 펴현된다.
        super().__init__(name)



from abc import ABC, abstractmethod

# abstractmethod 는 상속을 받을 클래스에서 무조건 들고 가야하는 함수를 강제한다.
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, name) :
        self.name = name

# 까먹고 구현을 하지 않음을 방지하는 abstractmethod이다
    def sound(self):
        print("멍멍")

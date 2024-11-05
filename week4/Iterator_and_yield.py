


# Iterator
# Iterable
# Generator
# Yield


# 리스트또는 컬렉션 데이터 사용

numbers = [1,2,3,4,5]

for num in numbers:
    print(num)


# __iter__()는 이터레이터 자신을 반환하는 메서드이다.
iterator = iter(numbers)


# __next__()는 이터레이터의 다음 요소를 반환한다. 즉 iterator는 1,2,3,4,5이기에 한번 실행하면, 1 두번은 2로 
# 순서대로 반환하며, 5가 나온 후 재실행을 하게되면 에러가 뜨게된다. (StopIteration)
next(iterator)



# 이터레이터 구현 예시
class MyIterator :
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
# raise는 의도적으로 에러를 발생 시킨다. 
            raise StopIteration
        

my_iter = MyIterator([1,2,3])





class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Bob")

for a  in my_iter:
    print(a)



def generate_5():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = generate_5()
print(next(gen))


def test_function():
    a = 1
    a+= 1
    return a


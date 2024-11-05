# 리스트
# 여러개의 항목을 저장 할 수 있는 가변 자료형
# []로 구분을 한다

number_list = [1,2,3,4,5]
print(number_list[0:2])

# []안의 0:2는 0번째 부터 2번째 이전 까지 표현해 달라고 하는 것이다.
# >> [1, 2] 을 나타낸다.

print(number_list[-1])
# 음수를 넣게 되면 뒤에서 부터 카운트가 들어간다. 이때는 -1이 제일 뒷 번호가 된다.

number_list[0] = "이승열"
print(number_list)
# 가변 자료형 이기 떄문에, 데이터 타입이 달라도 변경이 된다.
# 하지만 [0]을 "승열"로 바꾸면 에러가 뜨는데 이는 문자열인 string은 불변자료형이라 그렇다.

number_list[0] = 1

number_list.append(6)
# append는 ()안의 값을 우측에 추가한다.

number_list.remove(6)
# remove는 ()안의 값을 없앤다.

length = len(number_list)
print(length)
# len은 리스트 안의 값의 갯수를 센다.

number_list.sort()
# sort는 리스트의 값을 순서대로 정리해준다.


# 튜플
# 리스트와 유사 하지만, 불변 자료형이다.
# 튜플은 (( ))으로 표현됨.
number_tuple = (1,2,3,4)

print(number_tuple)

# 리스트의 인덱스 또한 사용가능 number_tuple[0] >> 1  / len 또한 사용 가능
# number_tuple[0] = 10 같이 변경을 필요한 것은 불가능 append또한 불가능



# 딕셔너리
name_dict = {"name": "승열", "age": 26}
# 여기서 name과 age는 키, 승열과 26은 값이다.

del name_dict["age"]
# del 로 age키를 삭제하기

name_dict.keys()
# 존재하는 키들을 불러오기
name_dict.values()
# 존재하는 값을 불러오기



# 셋
# 집합을 나타내는 자료형. 중복이 없고 순서가 없다.

number_set = {1,2,3,4,5,6,6}
# >>{1,2,3,4,5,6} 중복 데이터는 삭제됨

number_set.add(7)
# add로 추가하기

number_set.remove(1)
# 값을 직접적으로 삭제하기

number_set2 = {1,2,3}

number_set.union(number_set2)
# 합집합 {1,2,3,4,5,6}

number_set.intersection(number_set2)
# 교집합 {1,2,3}



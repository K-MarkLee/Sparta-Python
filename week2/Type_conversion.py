# 명시적 타입 변환

float_sample = 3.14
string_sample = "100"

int(float_sample) 
# >> 3
int(string_sample)
# >> 100
# 적절히 숫자로 변경해줌

int_sample = 10
string_sample_2 = "3.14"

float(int_sample)
# 10.0
float(string_sample_2)
# 3.14


bool_test_1 = 0
bool_test_2 = ""
bool(bool_test_1)
# False
bool(bool_test_2)
# Fasle
# 빈 값이나 0은 False로 표시


list_sample = [1,2,3,4,4]
set(list_sample)
# >> {1,2,3,4}  set은 중복 허용하지 않기 때문에 4는 합쳐짐
tuple(list_sample)
# 딕셔너리는 키가 필요해서 불가능

name = "이승열"
# name[0] = 김 은 불가능.

name_list = list(name)
name_list[0] = "김"
print(name_list)
# 리스트로 변경을 한 수에는 가능.



# 암시적 타입 변환
# 자동적으로 변환되는 경우

# float > int 의 경우 소수점 사라짐 주의

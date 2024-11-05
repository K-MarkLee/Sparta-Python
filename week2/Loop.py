# for 문
list_sample = [2,4,6,8,10]

for element in list_sample:
    print(element)
# 튜플과 문자열 또한 가능

for number in list_sample:
    square = number ** 2
    print(f"{number}의 제곱은 {square}입니다.")




# while 문
age = 10
while age < 20:
    print(f"{age}살이되었습니다.")
    age = age + 1


n = 1
end_condition = True
while end_condition:
    end_condition = int(input("종료를 위해서 0을 입력해 주세요"))
    print(f"반복중입니다.")
    


while n < 100 :
    condition = int(input("1을 입력하면 중지됩니다."))
    if condition == 1:
        continue
    n += 1

print(n)



# for문

for i in range(0,10,1):
    print(i)
# ()안의 0은 첫값, 10은 끝값 1은 +되는 양
# ()1개의 숫자만 있다면 끝값\

for i,j in enumerate(list_sample):
    print(i,j)

# 0  2 / 1  4 ... 이렇게 된다.



#중첩 반복문
for i in range(1,10):
    print(f"{i}단: ")
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")
    print()


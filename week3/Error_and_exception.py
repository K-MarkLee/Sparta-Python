# 코드 상에서 에러가 있다면, 그 아래의 코드는 작동하지 않고 멈출 것이다.
# 이때 에러는 열려고 하는 파일이 존재하지 않거나, 값이 나오지 않는 즉 숫자를 0으로 나누는 등에 해당한다.

# 이때 예외를 처리해서 프로그램이 멈추지 않고 예외처리를 하여 계속 실행되게 할 수 있다.

try: 
    print("test_before")
    open("test.txt", "r")
    print(10/0)
except ZeroDivisionError:
    print("0으로 나눴습니다.")

except FileNotFoundError:
    print("파일이 없습니다")

except:
    print("모든 예외")
finally:
    print("test_after")


# 이때 except가 발생한 코드를 기점으로 뒤의 코드는 실행되지 않는다.
# finally를 사용하면 에러가 나더라고 실행이 된다.

# 에러의 내용이 많거나 다양한 경우 except만으로 대응 하기 어려울 수 있다.
# 하지만 프로그램의 안전성은 except만으로 매우 높일 수 있다.

try:
    10/0
except Exception as e :
    print(f"모든에러 {e}")

# Exception을 사용하여 모든 에러를 나타 낼 수도 있다.
# 이들은 에어가 생겼을때의 임시처리이지 대응이 아니기 떄문에 처리를 따로 해줘야 한다.


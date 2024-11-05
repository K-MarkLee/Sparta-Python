# 모듈이란 함수, 클래스, 변수 등을 묶어둔 코드 묶음을 뜻한다.
# 하나의.py파일이 모듈이 될 수 있다.

# 코드의 유사성 별로 분류하고 불러오면 관리가 용이하고 재사용 하기 쉽다.

import My_module 

My_module.greet("Mark")
# My_module 에 있는 greet함수를 불러오는 것이다.

from My_module import getage as a

a(16)

# 이렇게 함수만 꺼내 올 수도 있다. 함수를 다른 이름으로 지정하기도 가능

# 패키지는 모듈의 묶음 이다. 이때 패키지의 디렉토리 안에는 __init__.py파일이 존재해야 패키지로 인식은 한다.
# 패키지를 불러오는 방식은 아래와 같다.

# from package import module
# from package.module import function

# 모듈을 사용 할 때에는, 이름의 충돌의 주의해야한다.

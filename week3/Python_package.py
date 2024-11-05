# 패키지 설치하기
# 패키지는 터미널에서 설치를 해야한다 
# pip install 패키지이름

import numpy

a = numpy.array([1,2,3,4,5])
print(a+10)

# >>[11,12,13,14,15]
# numpy를 이용하면, 이렇게 어려운 것도 쉽게 할 수 있다.
# 원래라면 불가능

# 가상화 하기 python =m venv 이름(myenv)
# 실행하기 이름(myenv)\\Scripts\\Activate
# 끄기 deactivate

# 현재 설치된 pip리스트 작성하기
# pip freeze > requirements.txt

# requirements 문서로 pip설치하기
# pip install -r requirements.txt

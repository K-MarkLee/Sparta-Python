

# 파일 경로로 열기
# 읽어온다는 의미로 r을 추가 (r을 넣지 않아도 기본적으로 실행이됨)
# r은 read
file = open("꿀잼개그.txt","r",encoding='UTF-8')

# cp949 에러 발생 > utf-8f로 변경
# read는 파일의 전체를 불러옴 (크기가 크면 문제 가능성 있음)
print(file.read())

# read의 방식으로 글을 읽으면, 포인터라고 하는것이 맨 마지막 줄로 가게 되어서 
# readline을 사용하려면 포인트를 초기화 시켜줘야한다. 
file.seek(0)

# 한줄씩 불러옴
print(file.readline())

file.seek(0)
# 라인을 리스트로 보관함.
linelist = file.readlines()
print(linelist)

file.seek(0)
# 리스트 형식으로 보관 후 쉽게 꺼내기 가능.
for line in linelist :
    print(line)


# 실행 후 파일을 닫지 않으면, 손실이나 잠금이 될 수 있다.

# 파일 닫기
file.close()


file = open("꿀잼개그.txt","w",encoding='UTF-8')

# lines = ["첫 번째 중\\n", "두 번쨰 줄\\n" ,"세 번째 중\\ n" ]

# \n은 각 문장을 줄바꿈해줌.\n는 사라짐
lines = ["첫 번째 줄\n", "두 번쨰 줄\n" ,"세 번째 줄 \n" ]

# write는 파일이 있으면, 덮어씀
file.write("한줄 추가")
print(file)

# file.close()

# w는 파일이 없더라도 생성
# w는 write를 의미
a = open("없는파일.txt", "w")
file.writelines(lines)
file.close()
a.close()

# 파일 경로 확인해야함
# 파일은 항상 닫아야함
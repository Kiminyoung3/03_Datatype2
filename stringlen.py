#문자열 길이 구하기
hello_world = "엄마가 말했다. '밥 먹었니?'"
print(len(hello_world))

print("-"*20)


#문자열 슬라이싱
자유로운_문자열 = "서울특별시 관악구 시흥대로 558-1"
print(len(자유로운_문자열))
print(자유로운_문자열[7:13])

print("-"*20)

# 문자열 치환
date = "2020.10.23"
print("바꾸기 전의 데이터: " + date)
date = date.replace(".", "-")
print("바꾼 후의 데이터: " + date)

print("-"*20)

#문자열 여러줄 출력하기
#한 줄 쓰고 \n 그 다음 줄을 쓴다.
print("아무 문장이나 입력해보세요. \n저는 지금 너무 졸린데, 집에 보내주세요.")

print("-"*20)

#숫자열
num_1 = 1
num_2 = "1"

print(num_1*5)
print(num_2*5)


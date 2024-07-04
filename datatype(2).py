#변수 할당 방법 = ctrl + /
b = a = 100
print(a)
print(b)

c,d = 50,100
print(c, d)

print('-'*20)
#문자열 반복

a = 'pig'
b = 'bed'
result = a+b
c = a + '@@@' + b
d = 3
space = '     '

print(a,b)
print("a"+"b")
print(result)
print(a, space, b)

print(a*d)
print(a, b, c +'&&&')

print('-'*20)
#변수를 이용해 이동거리 구하기
#거리 = 속도*시간

speed = 3
time = 15
distance = speed*time

print(distance)
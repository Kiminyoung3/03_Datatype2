#1번: 변수에 데이터 넣기
a = 7
b = 3
result = a+b
print(result)

print("-"*20)

#2번

print("-"*20)

#3번

print("-"*20)

#4번

print("-"*20)

#5번: 문자열 거꾸로 출력
aa = "Python"
print(aa[-1],aa[-2],aa[-3],aa[-4],aa[-5],aa[-6])

bb = aa[-1]+aa[-2]+aa[-3]+aa[-4]+aa[-5]+aa[-6]
print(bb)

alist = ["P", "y", "t", "h", "o", "n"]
print(alist[5]+alist[4]+alist[3]+alist[2]+alist[1]+alist[0])

print("-"*20)

#6번: 문자열 치환
data = "abcd"
print(data)
data = data.replace("a", "A")
print(data)

print("-"*20)

#7번: 리스트의 평균 출력
nums = [1, 2, 3, 4, 5] #또는 nums = list(range(1, 6))
print(len(nums))

a = nums[0]+nums[1]+nums[2]+nums[3]+nums[4] #average = nums / len(nums)
print(a)
print(a/5)

print("-"*20)

fruits = {"apple":3, "banana":5, "cherry":2}
print(fruits["banana"])

#8번
#한국, 미국, 중국의 위도, 경도 데이터

country = {"한국":[37, 127] , "미국":[25, 66] , "중국":[18, 109]}

print(country["한국"][1])
print(country["중국"][0])

dic_1 = {"a": {"b": 1, "c": 2}}
print(dic_1["a"]["c"])

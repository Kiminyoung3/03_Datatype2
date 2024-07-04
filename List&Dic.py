print("-"*20)

#리스트와 인덱싱
a = [1, 2, 3]
print(type(a))
print(a[1])

print("-"*20)

#리스트의 수열 생성하기
#range(n) 함수는 0부터 n-1까지 1씩 증가하는 수의 집합을 만든다.
#range 함수로 생성한 수열을 전부 출력하려면 print(list(range(n)))
#수열을 리스트로 생성하려면: list(range(시작번호, 끝번호, 증가하는 크기)) > 마지막 숫자는 포함하지 않음.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(list(range(10)))

print(list(range(0, 30, 3)))

#리스트명.append() 함수 사용: 리스트에 요소 추가
#리스트명.remove() 함수 사용: 리스트에 요소 삭제
num_list = [1, 2, 3, 4, 5]
print(num_list)
num_list.append(6)
print(num_list)
num_list.remove(3)
print(num_list)



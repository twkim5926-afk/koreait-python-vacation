# 내장 함수
# sum(리스트) -> 다 더한 결과 리턴
nums = [1, 2, 3, 4]
result = sum(nums)
print(result)

min_val = min(nums)
max_val = max(nums)

# all([]):모두 True -> True : 전체 and연산
# any([]):하나라도 True-> True : 전체 or연산

my= "가위"
com= "보"

win1 = my == "가위" and com == "보"
win2 = my == "바위" and com == "가위"
win3 = my == "보" and com == "바위"
wins = [win1, win2, win3]
print("승리?", True in wins)
print("승리?", any(wins ))

numbers = [1, 3, 5, 8]
# 짝수가 하나라도 있는가?
result = any([n % 2 == 0 for n in numbers])
print(result)

### 함수의 변수 생존범위(스코프)
# 1. 함수안에 선언된 변수는 함수안에서만 생존
# 2. 일반변수는 함수안에서 읽기'만'가능
# 3. 일반변수를 함수안에서 병경시 global
x = 10
def print_x():
    global x # 일반변수 x를 지정
    x += 1 # 변경 가능해진다!
    print(x)











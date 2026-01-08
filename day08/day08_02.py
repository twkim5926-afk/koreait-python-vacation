dialog = ("솔직히 말해서 솔직히 저는 이게 맞는지 모르겟습니다. "
          "솔직히 근데 그냥 솔직히 귀찮습니다.")
word = "솔직히"

# "솔직히" 라는 단어는 몇번 반복되는지?
count = 0
len_of_word = len(word)
len_of_dialog = len(dialog)
for  i in range(len_of_word):
    tmp = dialog[i:i + len_of_word]
    if tmp == word:
        count += 1
print(f"솔직히가 등장한 횟수: {count}")

# -> 문장과 단어를 매개변수로 받고
# 단어가 문장안에서 몇번 등장하는지 리턴하는 함수
def count_repeat(dialog, word):
    count = 0
    len_of_word = len(word)
    len_of_dialog = len(dialog)
    for i in range(len_of_word):
        tmp = dialog[i:i + len_of_word]
        if tmp == word:
            count += 1

    return count
count = count_repeat("솔직히 솔직히", "솔직히")
print(count)


# 할인계산기

menu = {
    1: ("아메리카노", 2500),
    2: ("카푸치노", 4000),
    3: ("바닐라라떼", 3500)
}

menu_choice = input("메뉴를 선택하세요(1~3)>")
menu_choice = int(menu_choice) # 숫자로 변환

menu_name, price = menu[menu_choice]
print(f"내가고른메뉴: {menu_name}, 가격:{price}")

day = input("오늘은 무슨 요일인가요(월~일) >")
# day와 price를 매개변수로 전달받아서
# 월:10퍼, 화~금:5퍼, 토~일:20퍼
# 적용해서 최종가격을 리턴하는 함수
def calc_week_discount(day, price):
    if day == "월":
        return price * 0.9
    elif day == ["토", "일"]:
        return price * 0.8
    else:
        return price * 0.95
print(f" {calc_week_discount(day, price)}")






















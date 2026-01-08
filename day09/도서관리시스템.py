books = []
# { "book_id": "1", "book_name": "파이썬책" }
# [ {},{},{}...{}]

while True:
    print("== 도서관리 시스템 ==")
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 삭제")
    print("q. 종료")

    selected_menu = input("메뉴를 선택 >>")
    if selected_menu == "1":
        book = input("등록할 도서의 이름을 입력하세요 >>")

        book = {
            "book_name": book,
        }
        books.append(book)
        print("도서가 등록되었습니다.")

        book_name = False
        for book in books:
            if book["book_name"] == book_name:
                book_name = True
                print("이미 존재하는 아이디입니다")
                break

    elif selected_menu == "2":
        if not books:
            print("등록된 도서가 없습니다")
            continue

        for book in books:
            book_name = book["book_name"]
            name = book["book_name"]
            print(f"{book_name}:도서명")

    elif selected_menu == "3":
        book_name = input("삭제할 도서명을 입력해주세요>>")
        found = False

        for book in books:
            if book["book_name"] == book_name:
                found = True
                books.remove(book)
                print("도서가 삭제 되었습니다.")
                break

        if not found:
            print("해당 도서를 찾을 수 없습니다.")

    elif selected_menu == "q":
        print("시스템을 종료 합니다.")
        break
    else:
        print("잘못된 일력입니다, 다시 입력해주세요")
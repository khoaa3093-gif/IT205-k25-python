hashtags = []
username = ""
title = ""
description = ""

while True:
    print("\n=== HỆ THỐNG KIỂM DUYỆT NỘI DUNG TIKTOK ===")
    print("1.Nhập dữ liệu và xem thống kê")
    print("2.Chuẩn hóa tên tài khoản TikTok")
    print("3.Kiểm tra hashtag hợp lệ")
    print("4.Tìm kiếm và thay thế từ khóa")
    print("5.Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    if choice == 1:
        username = input("Nhập tên tài khoản: ").strip()
        title = input("Nhập tiêu đề video: ").strip()
        description = input("Nhập mô tả video: ").strip()

        if username == "":
            print("Tên tài khoản không được rỗng")
            continue

        if description.strip() == "":
            print("Mô tả video không được rỗng")
            continue

        hashtag_input = input("Nhập hashtag (cách nhau bởi dấu ,): ").strip()

        hashtags = []
        if hashtag_input != "":
            hashtags = [h.strip() for h in hashtag_input.split(",")]

        print("\n--- THỐNG KÊ ---")
        print("Username:", username.strip())
        print("Title:", title.strip().title())
        print("Description:", description.strip())

        print("Độ dài mô tả:", len(description))
        print("Số từ trong mô tả:", len(description.split()))

        print("Hashtags:", hashtags)
        print("Số hashtag:", len(hashtags))

        print("Mô tả lowercase:", description.lower())
        print("Mô tả uppercase:", description.upper())

    elif choice == 2:
        name = input("Nhập tên tài khoản: ").strip()

        if name == "":
            print("Tên tài khoản không được rỗng")
        else:
            print("Ban đầu:", name)
            print("Chuẩn hoá:", "@" + name.lower())

    elif choice == 3:
        tag = input("Nhập hashtag: ").strip()

        error = ""

        if tag == "":
            error = "Hashtag không được rỗng"
        elif not tag.startswith("#"):
            error = "Hashtag phải bắt đầu bằng #"
        elif " " in tag:
            error = "Hashtag không được chứa khoảng trắng"
        elif len(tag) < 2:
            error = "Hashtag phải có ít nhất 2 ký tự"
        else:
            content = tag[1:]
            if not content.replace("_", "").isalnum():
                error = "Hashtag chỉ gồm chữ, số hoặc _"

        if error != "":
            print(error)
        else:
            print("Hashtag hợp lệ")
            hashtags.append(tag)

    elif choice == 4:
        find_word = input("Nhập từ khóa cần tìm: ").strip()
        replace_word = input("Nhập từ khóa thay thế: ").strip()

        if find_word in description:
            count = description.count(find_word)
            description = description.replace(find_word, replace_word)

            print("Mô tả sau khi thay thế:", description)
            print("Số lần xuất hiện:", count)
        else:
            print("Không tìm thấy từ khóa")

    elif choice == 5:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ!")
discount_list = []
shop_name = ""
product_name = ""
product_description = ""
category = ""

while True:
    print("\n=== HỆ THỐNG QUẢN LÝ SẢN PHẨM SHOPEE ===")
    print("1.Nhập dữ liệu và thống kê")
    print("2.Chuẩn hóa tên shop")
    print("3.Kiểm tra mã giảm giá")
    print("4.Tìm kiếm và thay thế từ khóa")
    print("5.Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    if choice == 1:
        shop_name = input("Tên shop: ").strip()
        product_name = input("Tên sản phẩm: ").strip()
        product_description = input("Mô tả sản phẩm: ").strip()
        category = input("Danh mục: ").strip()
        keywords_input = input("Danh sách từ khóa (cách nhau dấu ,): ").strip()

        if shop_name == "":
            print("Tên shop không được bỏ trống")
            continue

        if product_description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        keywords = []
        if keywords_input != "":
            keywords = [k.strip() for k in keywords_input.split(",")]

        print("\n=== THỐNG KÊ SẢN PHẨM ===")
        print("Shop:", shop_name.strip())
        print("Product:", product_name.strip().title())
        print("Description:", product_description.strip())
        print("Length description:", len(product_description))
        print("Category:", category.strip().lower())
        print("Keywords:", keywords)
        print("Number of keywords:", len(keywords))
        print("Lower:", product_description.lower())
        print("Upper:", product_description.upper())

    elif choice == 2:
        shop = input("Nhập tên shop: ").strip()

        if shop == "":
            print("Tên shop không được bỏ trống")
        else:
            shop_clean = shop.lower().replace(" ", "-")

            if not shop_clean.startswith("shop-"):
                shop_clean = "shop-" + shop_clean

            print("Ban đầu:", shop)
            print("Chuẩn hóa:", shop_clean)

    elif choice == 3:
        code = input("Nhập mã giảm giá: ").strip()

        error = ""

        if code == "":
            error = "Mã giảm giá không được rỗng"
        elif " " in code:
            error = "Mã giảm giá không được chứa khoảng trắng"
        elif len(code) < 6 or len(code) > 12:
            error = "Mã giảm giá phải từ 6-12 ký tự"
        elif not code.isalnum():
            error = "Mã giảm giá chỉ chứa chữ và số"
        elif not code.isupper():
            error = "Mã giảm giá phải viết hoa"
        elif not code.startswith("SALE"):
            error = "Mã giảm giá phải bắt đầu bằng SALE"

        if error != "":
            print(error)
        else:
            print("Mã giảm giá hợp lệ")
            discount_list.append(code)
            print("Danh sách mã giảm giá:", discount_list)

    elif choice == 4:
        if product_description.strip() == "":
            print("Chưa có mô tả sản phẩm")
            continue

        find_word = input("Từ khóa cần tìm: ").strip()
        replace_word = input("Từ khóa thay thế: ").strip()

        if find_word in product_description:
            count = product_description.count(find_word)
            product_description = product_description.replace(find_word, replace_word)

            print("Số lần xuất hiện:", count)
            print("Mô tả sau khi thay thế:", product_description)
        else:
            print("Không tìm thấy từ khóa")

    elif choice == 5:
        print("Thoát chương trình")
        break

else:
    print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
sender_name = ""
sender_phone = ""
pickup_address = ""
receiver_name = ""
receiver_phone = ""
delivery_address = ""
note = ""

while True:
    print("\n=== QUẢN LÝ ĐƠN HÀNG ===")
    print("1.Nhập dữ liệu đơn hàng")
    print("2.Chuẩn hóa mã đơn hàng")
    print("3.Ẩn số điện thoại")
    print("4.Tìm kiếm và thay thế ghi chú")
    print("5.Thoát")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    if choice == 1:
        sender_name = input("Tên người gửi: ").strip()
        sender_phone = input("SĐT người gửi: ").strip()
        pickup_address = input("Địa chỉ lấy hàng: ").strip()
        receiver_name = input("Tên người nhận: ").strip()
        receiver_phone = input("SĐT người nhận: ").strip()
        delivery_address = input("Địa chỉ giao hàng: ").strip()
        note = input("Ghi chú: ").strip()

        if sender_name == "":
            print("Tên người gửi không được bỏ trống")
            continue
        if receiver_name == "":
            print("Tên người nhận không được bỏ trống")
            continue
        if pickup_address == "":
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue
        if delivery_address == "":
            print("Địa chỉ giao hàng không được bỏ trống")
            continue
        if note == "":
            print("Ghi chú không được bỏ trống")
            continue

        print("\n=== THÔNG TIN ĐƠN HÀNG ===")
        print("Người gửi:", sender_name.strip().title())
        print("Người nhận:", receiver_name.strip().title())
        print("Địa chỉ lấy:", pickup_address.strip())
        print("Địa chỉ giao:", delivery_address.strip())
        print("Ghi chú:", note)
        print("Độ dài ghi chú:", len(note))
        print("Số từ:", len(note.split()))
        print("Lower:", note.lower())
        print("Upper:", note.upper())

    elif choice == 2:
        code = input("Nhập mã đơn hàng: ").strip()

        code = code.upper().replace(" ", "-")

        if not code.startswith("GRAB-"):
            code = "GRAB-" + code

        print("Mã sau chuẩn hóa:", code)

    elif choice == 3:
        def mask(phone):
            if phone == "":
                return "Số điện thoại không hợp lệ"
            if not phone.isdigit():
                return "Số điện thoại không hợp lệ"
            if len(phone) != 10:
                return "Số điện thoại không hợp lệ: phải đủ 10 số"
            return phone[:3] + "*****" + phone[-2:]

        print("SĐT người gửi:", mask(sender_phone))
        print("SĐT người nhận:", mask(receiver_phone))

    elif choice == 4:
        if note.strip() == "":
            print("Chưa có ghi chú để tìm kiếm")
            continue

        find_word = input("Từ khóa cần tìm: ").strip()
        replace_word = input("Từ khóa thay thế: ").strip()

        if find_word in note:
            count = note.count(find_word)
            note = note.replace(find_word, replace_word)

            print("Số lần xuất hiện:", count)
            print("Ghi chú sau thay thế:", note)
        else:
            print("Không tìm thấy từ khóa")

    elif choice == 5:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ!")
order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    print("\n=== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS ===")
    print("1.Hiển thị danh sách đơn hàng")
    print("2.Gán tài xế cho đơn hàng")
    print("3.Cập nhật trạng thái giao hàng")
    print("4.Hủy đơn hàng")
    print("5.Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            count = 1
            for order in order_list:
                print(str(count) + ". " + order)
                count += 1

    elif choice == "2":
        code = input("Nhập mã đơn hàng cần gán tài xế: ").strip().upper()

        check = False

        for i in range(len(order_list)):
            data = order_list[i].split(" - ")

            if data[0] == code:
                check = True

                if data[1] == "PENDING":
                    order_list[i] = data[0] + " - ASSIGNED"
                    print("Gán tài xế thành công.")
                else:
                    print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")

                break

        if check == False:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == "3":
        code = input("Nhập mã đơn hàng cần cập nhật: ").strip().upper()

        check = False

        for i in range(len(order_list)):
            data = order_list[i].split(" - ")

            if data[0] == code:
                check = True

                if data[1] == "ASSIGNED":
                    order_list[i] = data[0] + " - DELIVERING"
                    print("Đã chuyển sang trạng thái DELIVERING")

                elif data[1] == "DELIVERING":
                    order_list[i] = data[0] + " - COMPLETED"
                    print("Đã chuyển sang trạng thái COMPLETED")

                elif data[1] == "PENDING":
                    print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")

                elif data[1] == "COMPLETED":
                    print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")

                elif data[1] == "CANCELLED":
                    print("Đơn hàng đã bị hủy, không thể cập nhật.")

                break

        if check == False:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == "4":
        code = input("Nhập mã đơn hàng cần hủy: ").strip().upper()

        check = False

        for i in range(len(order_list)):
            data = order_list[i].split(" - ")

            if data[0] == code:
                check = True

                if data[1] == "PENDING" or data[1] == "ASSIGNED":
                    order_list[i] = data[0] + " - CANCELLED"
                    print("Hủy đơn hàng thành công.")

                elif data[1] == "DELIVERING":
                    print("Đơn hàng đang được giao, không thể hủy.")

                elif data[1] == "COMPLETED":
                    print("Đơn hàng đã hoàn tất, không thể hủy.")

                else:
                    print("Đơn hàng đã được hủy trước đó.")

                break

        if check == False:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == "5":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
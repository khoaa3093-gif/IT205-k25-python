order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n=== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS ===")
    print("1.Hiển thị danh sách đơn hàng")
    print("2.Cập nhật danh sách đơn hàng")
    print("3.Thống kê đơn hàng theo trạng thái")
    print("4.Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                print(i + 1, ".", order_list[i], sep="")

    elif choice == "2":
        print("\n1.Thêm đơn hàng mới")
        print("2.Sửa đơn hàng theo vị trí")
        print("3.Xóa đơn hàng theo vị trí")
        print("4.Quay lại")

        sub_choice = input("Chọn chức năng: ")

        if sub_choice == "1":
            code = input("Nhập mã đơn hàng: ").strip().upper()
            status = input("Nhập trạng thái: ").strip().upper()

            order_list.append(code + " - " + status)
            print("Thêm thành công")

        elif sub_choice == "2":
            pos = input("Nhập vị trí cần sửa: ")

            if pos.isdigit():
                pos = int(pos)
                if 1 <= pos <= len(order_list):
                    code = input("Nhập mã mới: ").strip().upper()
                    status = input("Nhập trạng thái mới: ").strip().upper()

                    order_list[pos - 1] = code + " - " + status
                    print("Sửa thành công")
                else:
                    print("Không tồn tại đơn hàng ở vị trí này!")
            else:
                print("Vị trí không hợp lệ!")

        elif sub_choice == "3":
            pos = input("Nhập vị trí cần xóa: ")

            if pos.isdigit():
                pos = int(pos)
                if 1 <= pos <= len(order_list):
                    deleted = order_list.pop(pos - 1)
                    print("Đã xóa:", deleted)
                else:
                    print("Không tồn tại đơn hàng ở vị trí này!")
            else:
                print("Vị trí không hợp lệ!")

        elif sub_choice == "4":
            continue

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

    elif choice == "3":
        pending = 0
        delivering = 0
        completed = 0
        cancelled = 0

        for order in order_list:
            status = order.split(" - ")[1]

        if status == "PENDING":
                pending += 1
        elif status == "DELIVERING":
                delivering += 1
        elif status == "COMPLETED":
                completed += 1
        elif status == "CANCELLED":
                cancelled += 1

        print("\n=== THỐNG KÊ ĐƠN HÀNG ===")
        print("PENDING:", pending)
        print("DELIVERING:", delivering)
        print("COMPLETED:", completed)
        print("CANCELLED:", cancelled)
        print("Tổng số đơn hàng:", len(order_list))

    elif choice == "4":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
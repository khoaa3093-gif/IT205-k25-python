#bt4

def main():
    ma_bn = input("Nhập mã bệnh nhân: ").strip()
    nhiet_do = float(input("Nhập nhiệt độ cơ thể: "))
    nhip_tim = int(input("Nhập nhịp tim: "))

    print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
    print(f"Mã bệnh nhân: {ma_bn}")
    print(f"Nhiệt độ cơ thể: {nhiet_do} độ C")
    print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(nhiet_do)}")
    print(f"Nhịp tim: {nhip_tim} nhịp/phút")
    print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(nhip_tim)}")
    print("--------------------------------------------------")
    print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")

    main()

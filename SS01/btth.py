#bt1
def main():
    ma_bn = input("Nhập mã bệnh nhân: ")
    ten_bn = input("Nhập tên bệnh nhân: ")
    gioi_tinh = input("Nhập giới tính: ")
    nam_sinh = int(input("Nhập năm sinh: "))
    sdt = input("Nhập số điện thoại: ")
    email = input("Nhập email: ")
    trieu_chung = input("Nhập triệu chứng ban đầu: ")
    chi_phi = int(input("Nhập chi phí khám: "))

    print("\n--- THẺ BỆNH NHÂN ---")
    print(f"Mã BN       : {ma_bn}")
    print()
    print(f"Tên         : {ten_bn} (str)")
    print(f"Giới tính   : {gioi_tinh} (str)")
    print(f"Năm sinh    : {nam_sinh} (int)")
    print(f"Điện thoại  : {sdt} (str)")
    print(f"Email       : {email} (str)")
    print(f"Triệu chứng : {trieu_chung} (str)")
    print(f"Chi phí     : {chi_phi}")

    main()



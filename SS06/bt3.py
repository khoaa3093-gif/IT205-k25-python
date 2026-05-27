for i in range(1, 4):
    print("--- NHẬP THÔNG TIN NHÂN VIÊN ---")
    
    ma_nv = input("Mã nhân viên: ")
    ho_ten = input("Họ và tên nhân viên: ")
    phong_ban = input("Phòng ban công tác: ")
    
    if ma_nv == "" or ma_nv == " " or ho_ten == "" or ho_ten == " ":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
    else:
        print("--- PHIẾU HỒ SƠ ĐIỆN TỬ ---")
        print("Mã nhân viên:", ma_nv)
        print("Họ và tên:", ho_ten)
        print("Phòng ban:", phong_ban)
        print("---------------------------")

print("Chương trình hoàn thành.")

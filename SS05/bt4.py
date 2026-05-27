print("———— HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ————")

while True:
    so_luong = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    if so_luong <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
    else:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {so_luong} nhân sự mới!")
        break

print("———— CHƯƠNG TRÌNH KẾT THÚC ————")

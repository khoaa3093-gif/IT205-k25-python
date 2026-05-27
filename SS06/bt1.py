print("—— PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ——")

total_budget = 0

for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input("  Nhập mức lương (VNĐ): "))
    total_budget = total_budget + salary

print("= KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")

# lối đặt total_budget ở trong vòng lập dẫn đến reset về 0 mỗi khi lập
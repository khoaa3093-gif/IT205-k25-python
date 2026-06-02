# LỖI LOGIC:
# Chương trình hiện tại đang dùng:
# - Vòng lặp ngoài duyệt theo tháng
# - Vòng lặp trong duyệt theo chi nhánh

# Điều này làm dữ liệu được nhóm theo tháng:
# Tháng 1 -> Chi nhánh 1, 2, 3
# Tháng 2 -> Chi nhánh 1, 2, 3
# ...

# Trong khi yêu cầu nghiệp vụ cần:
# Gom toàn bộ dữ liệu của từng chi nhánh lại với nhau

# Vì vậy:
# - Vòng lặp ngoài phải duyệt theo chi nhánh
# - Vòng lặp trong mới duyệt theo tháng

# Chương trình không sai cú pháp
# Nhưng sai logic xử lý dữ liệu theo yêu cầu báo cáo nghiệp vụ

# Sửa lỗi
print("=== HỆ THỐNG BÁO CÁO DOANH THU ===")

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

result = ""

for branch in range(1, branch_count + 1):
    result += f"\n--- Chi nhánh {branch} ---\n"
    for month in range(1, month_count + 1):
        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: ")
        )
        result += (
            f"Tháng {month}: {revenue} triệu đồng\n"
        )

print("\nKẾT QUẢ BÁO CÁO")
print(result)

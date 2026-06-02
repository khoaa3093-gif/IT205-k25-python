# LỖI LOGIC:
# Biến total_students được khai báo bên ngoài vòng lặp chi nhánh

# Điều này làm cho:
# Tổng học viên của chi nhánh trước
# bị cộng dồn sang chi nhánh sau

# total_students không được reset về 0
# khi chuyển sang chi nhánh mới

# Chi nhánh 1

# total_students ban đầu = 0

# Lớp 1: 30 học viên
# total_students = 0 + 30 = 30

# Lớp 2: 25 học viên
# total_students = 30 + 25 = 55

# Lớp 3: 28 học viên
# total_students = 55 + 28 = 83

# => Hiển thị đúng:
# Chi nhánh 1: 83 học viên

# Chi nhánh 2

# Đáng lẽ total_students phải reset về 0
# Nhưng thực tế vẫn đang giữ giá trị 83

# Lớp 1: 20 học viên
# total_students = 83 + 20 = 103

# Lớp 2: 18 học viên
# total_students = 103 + 18 = 121

# Lớp 3: 22 học viên
# total_students = 121 + 22 = 143

# => Hệ thống hiển thị:
# Chi nhánh 2: 143 học viên

# Nhưng thực tế đúng phải là:
# 20 + 18 + 22 = 60 học viên

# Chi nhánh 3

# total_students tiếp tục giữ giá trị 143

# Lớp 1: 35 học viên
# total_students = 143 + 35 = 178

# Lớp 2: 30 học viên
# total_students = 178 + 30 = 208

# Lớp 3: 32 học viên
# total_students = 208 + 32 = 240

# => Hệ thống hiển thị:
# Chi nhánh 3: 240 học viên

# Nhưng thực tế đúng phải là:
# 35 + 30 + 32 = 97 học viên

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của một chi nhánh: "))

for branch in range(1, branch_count + 1):
    total_students = 0
    print(f"\nChi nhánh {branch}")
    for classroom in range(1, class_count + 1):
        student_count = int(
            input(f"Nhập số học viên lớp {classroom}: ")
        )
        total_students += student_count
    print(f"Chi nhánh {branch}: {total_students} học viên")

# PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# INPUT:
# - branch_count:
#   Số lượng chi nhánh (kiểu int)

# - student_count:
#   Số học viên đi học của từng lớp (kiểu int)

# OUTPUT:
# - In trạng thái lớp học sau khi nhập dữ liệu
# - Hoặc hiển thị thông báo lỗi nếu dữ liệu không hợp lệ

# Ý TƯỞNG GIẢI PHÁP
# Mỗi chi nhánh có cố định 2 lớp học

# Dùng vòng lặp ngoài:
# duyệt từng chi nhánh

# Dùng vòng lặp trong:
# duyệt 2 lớp học của mỗi chi nhánh

# Với mỗi lớp:
# - nhập số học viên đi học
# - kiểm tra dữ liệu hợp lệ
# - in trạng thái lớp học

# XỬ LÝ EDGE CASES
# Edge Case 1:
# Nếu số học viên < 0
# => dữ liệu không hợp lệ
# => yêu cầu nhập lại bằng vòng lặp while

# Edge Case 2:
# Nếu số học viên == 0
# => lớp vắng toàn bộ
# => bỏ qua đánh giá lớp học bằng continue

# ĐÁNH GIÁ TRẠNG THÁI LỚP
# Nếu số học viên >= 20
# => "Lớp học ổn định"

# Nếu số học viên < 20
# => "Lớp cần được nhắc nhở theo dõi"

# THUẬT TOÁN
# Nhập số lượng chi nhánh
# Lặp qua từng chi nhánh
#     In tên chi nhánh
#     Lặp qua 2 lớp học
#         Nhập số học viên
#         Nếu số học viên < 0
#             Báo lỗi
#             Nhập lại
#         Nếu số học viên == 0
#             In thông báo lớp vắng toàn bộ
#             Bỏ qua đánh giá lớp
#         Nếu số học viên >= 20
#             In lớp học ổn định
#         Ngược lại
#             In lớp cần được nhắc nhở theo dõi

# Triển khai code
branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}:")
    for classroom in range(1, 3):
        while True:
            student_count = int(
                input(
                    f"Nhập số học viên đi học của lớp {classroom}: "
                )
            )
            if student_count < 0:
                print(
                    "Số học viên không hợp lệ. Vui lòng nhập lại."
                )

            else:
                break
        if student_count == 0:
            print(
                "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
            )
            continue
        if student_count >= 20:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                "Lớp học ổn định"
            )
        else:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                "Lớp cần được nhắc nhở theo dõi"
            )

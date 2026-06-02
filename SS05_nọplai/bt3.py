# PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

# INPUT:
# - room_count:
#   Số lượng phòng học (kiểu int)
# - row_count:
#   Số hàng ghế của mỗi phòng (kiểu int)
# - seat_count:
#   Số ghế trên mỗi hàng (kiểu int)

# OUTPUT:
# - In sơ đồ chỗ ngồi bằng dấu *
# - Hoặc hiển thị thông báo lỗi nếu dữ liệu không hợp lệ

# Ý TƯỞNG GIẢI PHÁP
# Bước 1:
# Nhập số lượng phòng học
# Nếu số lượng phòng <= 0
# => báo lỗi
# => kết thúc chương trình
# Bước 2:
# Dùng vòng lặp for để duyệt từng phòng học
# Bước 3:
# Với mỗi phòng:
# - nhập số hàng ghế
# - nhập số ghế mỗi hàng
# Bước 4:
# Kiểm tra dữ liệu hợp lệ
# Nếu số hàng hoặc số ghế <= 0
# => dữ liệu không hợp lệ
# => bỏ qua phòng hiện tại bằng continue
# Nếu số hàng hoặc số ghế > 10
# => phòng quá lớn
# => dừng toàn bộ chương trình bằng break
# Bước 5:
# Nếu dữ liệu hợp lệ:
# dùng vòng lặp lồng nhau để in sơ đồ ghế

# - Vòng ngoài:
#   duyệt theo từng hàng ghế

# - Mỗi lần lặp:
#   in "*" theo số ghế của hàng

# THUẬT TOÁN
# Nhập số lượng phòng

# Nếu số lượng phòng không hợp lệ
#     In thông báo lỗi
#     Kết thúc

# Lặp qua từng phòng

#     Nhập số hàng
#     Nhập số ghế

#     Nếu dữ liệu không hợp lệ
#         In thông báo
#         continue

#     Nếu phòng quá lớn
#         In thông báo
#         break

#     In sơ đồ ghế

#     Lặp theo từng hàng
#         In dấu * theo số ghế

room_count = int(input("Nhập số lượng phòng học: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")

else:

    for room in range(1, room_count + 1):

        print(f"\n--- Phòng học {room} ---")

        row_count = int(input("Nhập số hàng ghế: "))
        seat_count = int(input("Nhập số ghế mỗi hàng: "))
        if row_count <= 0 or seat_count <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue
        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break
        print("\nSơ đồ chỗ ngồi:")

        for row in range(row_count):
            print("*" * seat_count)

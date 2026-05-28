Total_number_of_products = 0
count_box = int(input("Nhập số lượng hộp: "))
while count_box :
    while True:
        count_pro = int(input("Nhập số lượng sản phẩm trong hộp: "))
        if count_pro < 0:
            print("Số lượng sản phẩm không hợp lệ, bỏ qua thùng này!")
        elif count_pro > 0:
            Total_number_of_products += count_pro
        elif count_pro == 0:
            Number_of_valid_packages += 1
        break

print("Tổng số sản phẩm: ", Total_number_of_products)
print("Số lượng hộp hợp lệ: ", Number_of_valid_packages)

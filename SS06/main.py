laptop = 0
phone = 0
tablet = 0

while True:
    print("\n===== QUẢN LÝ KHO =====")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    try:
        user_choice = int(input("Nhập vào lựa chọn của bạn: "))
    except:
        print("Vui lòng nhập số!")
        continue

    if user_choice <= 0 or user_choice >= 6:
        print("Nhập sai, vui lòng nhập lại!!!")
        continue

    if user_choice == 5:
        print("Thoát chương trình...")
        break

  
    if user_choice == 1:
        print("\n===== BÁO CÁO TỒN KHO =====")
        print(f"Laptop: {laptop}")
        print(f"Phone: {phone}")
        print(f"Tablet: {tablet}")

        print("\n===== BIỂU ĐỒ TỒN KHO =====")

        print(f"Laptop ({laptop}): ", end="")
        for i in range(laptop):
            print("*", end="")
        print()

        print(f"Phone ({phone}): ", end="")
        for i in range(phone):
            print("*", end="")
        print()

        print(f"Tablet ({tablet}): ", end="")
        for i in range(tablet):
            print("*", end="")
        print()

  
    elif user_choice == 2:

        while True:
            print("\nBạn muốn nhập hàng nào:")
            print("1. Laptop")
            print("2. Phone")
            print("3. Tablet")

            try:
                user_input = int(input("Nhập lựa chọn của bạn: "))
            except:
                print("Vui lòng nhập số!")
                continue

            if user_input < 1 or user_input > 3:
                print("Lựa chọn không hợp lệ!!!")
                continue

           
            while True:
                try:
                    quantity = int(input("Nhập vào số lượng muốn thêm: "))
                except:
                    print("Vui lòng nhập số!")
                    continue

                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                    continue

                break

            if user_input == 1:
                laptop += quantity
                print("Nhập Laptop thành công!")

            elif user_input == 2:
                phone += quantity
                print("Nhập Phone thành công!")

            else:
                tablet += quantity
                print("Nhập Tablet thành công!")

            break


    elif user_choice == 3:

        while True:
            print("\nBạn muốn xuất hàng nào:")
            print("1. Laptop")
            print("2. Phone")
            print("3. Tablet")

            try:
                user_input = int(input("Nhập lựa chọn của bạn: "))
            except:
                print("Vui lòng nhập số!")
                continue

            if user_input < 1 or user_input > 3:
                print("Lựa chọn không hợp lệ!!!")
                continue

      
            while True:
                try:
                    quantity = int(input("Nhập số lượng muốn xuất: "))
                except:
                    print("Vui lòng nhập số!")
                    continue

                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                    continue

                break

            
            if user_input == 1:
                if quantity > laptop:
                    print("Không đủ hàng!")
                else:
                    laptop -= quantity
                    print("Xuất Laptop thành công!")

            elif user_input == 2:
                if quantity > phone:
                    print("Không đủ hàng!")
                else:
                    phone -= quantity
                    print("Xuất Phone thành công!")

            else:
                if quantity > tablet:
                    print("Không đủ hàng!")
                else:
                    tablet -= quantity
                    print("Xuất Tablet thành công!")

            break

    elif user_choice == 4:
        print("\n===== CẢNH BÁO TỒN KHO =====")

        if laptop < 10:
            print(f"[CẢNH BÁO] Laptop sắp hết (Chỉ còn {laptop} sản phẩm)")

        if phone < 10:
            print(f"[CẢNH BÁO] Phone sắp hết (Chỉ còn {phone} sản phẩm)")

        if tablet < 10:
            print(f"[CẢNH BÁO] Tablet sắp hết (Chỉ còn {tablet} sản phẩm)")
    
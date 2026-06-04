vehicles = []
next_id = 1

while True:
    user_choice = input("""
====================================
   QUẢN LÝ BÃI XE - SMART BANKING
====================================
1. Thêm xe mới vào bãi
2. Hiển thị danh sách xe trong bãi
3. Xóa xe khỏi bãi ( khi ra xe)
4. Thoát chương trình
====================================
Vui lòng chọn một tùy chọn (1-4):""").strip()

    if user_choice == "4":
        print("Cảm ơn bạn đã sử dụng dịch vụ!")
        break
    if user_choice == "1":
        print("Bạn đã chọn thêm xe mới vào bãi.")
        while True:
            vehicle_type = input("Nhập loại xe: ").strip()
            if vehicle_type:
                break
            print("Loại xe không được để trống. Vui lòng nhập lại.")
        while True:    
            owner_name = input("Nhập chủ xe: ").strip()
            if owner_name:
                break
            print("Chủ xe không được để trống. Vui lòng nhập lại.")

        vehicle = {
            "id": next_id,
            "type": vehicle_type,
            "owner": owner_name,
        }
        vehicles.append(vehicle)
        print(f"Xe mới đã được thêm với ID {next_id}.")
        next_id += 1

    elif user_choice == "2":
        print("Bạn đã chọn hiển thị danh sách xe trong bãi.")
        if not vehicles:
            print("Hiện tại không có xe nào trong bãi.")
        else:
            list = f"|{'ID':<5} | {'Loại xe':<10} | {'Chủ xe':<15}|"
            print(list)
            print("-"*len(list))
            for vehicle in vehicles:
                print(f"|{vehicle['id']:<5} | {vehicle['type']:<10} | {vehicle['owner']:<15}|")
    elif user_choice == "3":
        print("Bạn đã chọn xóa xe khỏi bãi.")
        remove_input = input("Nhập ID xe cần xóa: ")
        if remove_input.isdigit():
            remove_id = int(remove_input)
            found = False
            for vehicle in vehicles:
                if vehicles["id"] == remove_id:
                    vehicles.remove(vehicle)
                    print(f"Đã xóa xe ID {remove_id}")
                    found = True
                    break
            if not found:
                print("ID không tồn tại trong bãi xe")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        continue
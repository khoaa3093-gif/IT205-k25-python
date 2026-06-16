        item = {
            "id": item_id,
            "name": name,
            "quantity": quantity
        }
inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]

while True :
    choice = input("""
    ========================================
        QUẢN LÝ KHO HÀNG - GROCERY STORE    
    ========================================
    1. Xem danh sách hàng tồn kho
    2. Nhập thêm hàng hóa mới
    3. Cập nhật số lượng tồn kho theo ID
    4. Thoát chương trình
    ========================================
    Lựa chọn của bạn(1-4):""")
    if choice == '4':
        print("Cảm ơn bạn đã sử dụng chương trình. Hẹn gặp lại!")
        break
    elif choice == '1':
        if not inventory:
            print("Kho hàng hiện đang trống!")
        else:
            print("=== DANH SÁCH HÀNG TỒN KHO ===")
            list = f"|{'ID':<5} | {'Tên hàng':<20} | {'Số lượng':<10}|"
            print(list)
            print("-"*len(list))
            for item in inventory:
            print(f"|{item['item_id']:<5} | {item['name']:<20} | {item['quantity']:<10}")
    elif choice == '2':
        print("Nhập hàng hóa mới")
        while True 
            item_id = input("Nhập mã hàng hóa (ID):").strip()
            if item_id :
                break
        while True 
            name = input("Nhập tên hàng hóa:").strip()
            if name :
                break    
        quantity = input("Nhập số lượng tồn kho")

    elif choice == '3':
        print("3")
    else :
        print("LỰA  CHỌN KHÔNG HỢP LỆ! VUI LÒNG CHỌN LẠI")
        continue            


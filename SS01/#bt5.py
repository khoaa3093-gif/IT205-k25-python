#bt5

def main():
    print("=========================================================")
    print("  CHÀO MỪNG BẠN ĐẾN VỚI KIOSK TỰ PHỤC VỤ - BV SỨC KHỎE VÀNG")
    print("  Vui lòng đọc kỹ hướng dẫn và nhập thông tin chính xác.")
    print("=========================================================\n")

    raw_name = input("✍️  Bước 1: Nhập Họ và Tên (Ví dụ: NGUYEN VAN A): ")
    raw_id = input("✍️  Bước 2: Nhập Mã bệnh nhân (Ví dụ: BN1024, BA9901): ")
    raw_temp = input("✍️  Bước 3: Nhập Nhiệt độ cơ thể (Ví dụ: 36.5 hoặc 37.2): ")
    raw_heart = input("✍️  Bước 4: Nhập Nhịp tim hiện tại (Ví dụ: 80 hoặc 95): ")
    raw_weight = input("✍️  Bước 5: Nhập Cân nặng của bạn (Ví dụ: 55.4 hoặc 68.0): ")
    raw_dept = input("✍️  Bước 6: Nhập Khoa muốn khám (Ví dụ: Khoa Noi, Khoa Nhi): ")

    patient_name = raw_name.strip().upper()
    patient_id = raw_id.strip().upper()
    department_target = raw_dept.strip()

    body_temperature = float(raw_temp)
    heart_rate = int(raw_heart)
    body_weight = float(raw_weight)

    print("\n" + "="*55)
    print("             PHIẾU KHÁM BỆNH ĐIỆN TỬ             ")
    print("="*55)
    print(f" Mã bệnh nhân   : {patient_id}")
    print(f" Họ và tên      : {patient_name}")
    print(f" Nơi chỉ định   : {department_target}")
    print("-"*55)
    print(" [ CHỈ SỐ SINH HIỆU LÂM SÀNG ]")
    print(f" 🩺 Nhiệt độ    : {body_temperature} °C")
    print(f" 🩺 Nhịp tim    : {heart_rate} nhịp/phút")
    print(f" 🩺 Cân nặng    : {body_weight} kg")
    print("-"*55)
    print(" TRẠNG THÁI: Khai báo thành công! Mời đến phòng đợi.")
    print("="*55)

    print("\n" + "[ SYSTEM LOG - IT DEPARTMENT ONLY ]")
    print("-" * 55)
    print(f" variable: patient_name      | type: {type(patient_name)}")
    print(f" variable: patient_id        | type: {type(patient_id)}")
    print(f" variable: department_target | type: {type(department_target)}")
    print(f" variable: body_temperature  | type: {type(body_temperature)}")
    print(f" variable: heart_rate        | type: {type(heart_rate)}")
    print(f" variable: body_weight       | type: {type(body_weight)}")
    print("-" * 55)

    main()

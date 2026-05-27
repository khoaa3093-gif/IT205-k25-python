print("[HỆ THỐNG KIOSK NHÂN SỰ ĐÃ KHỞI ĐỘNG]")

while True:
    print("\n[Nhập thông tin nhân viên]")
    
    while True:
        employee_id = input("1. Enter Employee ID: ")
        if employee_id.strip() == "":
            print("[!] LỖI: Mã nhân viên không được bỏ trống. Vui lòng nhập lại!")
        else:
            break
            
    while True:
        employee_name = input("2. Enter Full Name: ")
        if employee_name.strip() == "":
            print("[!] LỖI: Họ tên không được bỏ trống. Vui lòng nhập lại!")
        else:
            break

    while True:
        current_salary = float(input("3. Enter current Salary in VND (Number > 0): "))
        if current_salary <= 0:
            print("[!] LỖI: Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại!")
        else:
            break

    while True:
        performance_score = float(input("4. Enter Performance Score (1.0 to 5.0): "))
        if performance_score < 1.0 or performance_score > 5.0:
            print("[!] LỖI: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!")
        else:
            break

    while True:
        experience_years = int(input("5. Enter Year of Experience (Integer >= 0): "))
        if experience_years < 0:
            print("[!] LỖI: Số năm kinh nghiệm phải lớn hơn hoặc bằng 0!")
        else:
            break

    print("\n==========================================================")
    print("                    E-PROFILE CẬP NHẬT                    ")
    print("==========================================================")
    print(f" - ID: {employee_id}")
    print(f" - Name: {employee_name}")
    print(f" - Salary: {current_salary:,.0f} VND")
    print(f" - KPI Score: {performance_score} / 5.0")
    print(f" - Experience: {experience_years} years")
    print("==========================================================")

    print("\n==========================================================")
    print("                      IT SYSTEM LOG                       ")
    print("==========================================================")
    print(f" employee_id        | {type(employee_id)}")
    print(f" employee_name      | {type(employee_name)}")
    print(f" current_salary     | {type(current_salary)}")
    print(f" performance_score  | {type(performance_score)}")
    print(f" experience_years   | {type(experience_years)}")
    print("==========================================================")

    tiep_tuc = input("\nDo you want to enter another employee? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break

print("\nĐang tắt Kiosk... Tạm biệt!")

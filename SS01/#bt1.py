#bt2

def main():
    print('--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---')
    name_patient = input('Nhập tên bệnh nhân: ')
    age = int(input('Mời bạn nhập tuổi: '))
    symptom = input('Mời bạn nhập triệu chứng bệnh: ')

    print('\n-- PHIẾU KHÁM BỆNH ---')
    # Sửa lỗi: Truyền đúng biến vào từng dòng hiển thị tương ứng
    print('Tên bệnh nhân:', name_patient)
    print('Tuổi:', age)
    print('Triệu chứng:', symptom)

    main()

for i in range(3):
        password = input("Nhập mật khẩu: ")
        if password == "123456":
            print("Đăng nhập thành công!")
            break
        else:
            print("Mật khẩu sai, vui lòng nhập lại!")
else:             
        print("Bạn đã đăng nhập quá 3 lần, Tài khoản đã bị khóa!")

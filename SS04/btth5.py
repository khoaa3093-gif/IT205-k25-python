import random
	secret = random.randint(1, 100)


	print("=== Trò chơi Đoán Số ===")

		try:
			guess = int(input(f"Lượt {attempts+1}/{max_attempts} - Nhập dự đoán của bạn: "))
		except ValueError:
			print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

		if guess == secret:
			print(f"Chúc mừng! Bạn đã đoán đúng sau {attempts} lượt. Bạn nhận được quà đặc biệt!")
			break

		if guess < secret:
			print("Gợi ý: Số bạn nhập nhỏ hơn mã số may mắn.")
		else:
			print("Gợi ý: Số bạn nhập lớn hơn mã số may mắn.")

		if attempts >= max_attempts:
			print(f"Bạn đã hết {max_attempts} lượt. Mã số may mắn là {secret}. Chúc may mắn lần sau!")


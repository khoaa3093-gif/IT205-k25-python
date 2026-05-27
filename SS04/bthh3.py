prices = []
total_bill = int(input("Nhập tổng số lượng của hóa đơn: "))

for i in range(1, total_bill + 1):
    price = int(input(f"Nhập giá tiền của hóa đơn {i}: "))
    prices.append(price)

    print("Kết quả kiểm toán ca Rekkei Education")
    print("Hóa đơn có giá trị cao nhất:", max(prices))
    print("Hóa đơn có giá trị thấp nhất:", min(prices))

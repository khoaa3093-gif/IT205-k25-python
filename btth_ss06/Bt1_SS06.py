price_bill =   int(input("Nhập đơn giá: "))
Quantity_purchased = int(input("Nhập số lượng mua: "))
total_price = price_bill + Quantity_purchased
print("Tổng tiền phải trả: ", total_price)
if total_price > 1000000:
    discount = total_price * 0.1
    final_price = total_price - discount
    print("Bạn được giảm giá 10%. Số tiền phải trả sau khi giảm: ", final_price)
else :
    print("Bạn không được giảm giá. Số tiền phải trả: ", total_price)


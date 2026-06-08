cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]

title = "------ Chi tiết giỏ hàng ------"
header = f"|{'STT':<3} | " + f"{'Mã sản phẩm':<13} | " + f"{'Tên sản phẩm':<20} | " + f"{'Số lượng':<8} | " + f"{'Đơn giá':<10} | " + f"{'Thành tiền':<12}|"
print(title)
print(header)
print("="*len(header))


for serial_number, item in enumerate(cart_items, start=1):
    total_price = item["price"] * item["number"]
    print(f"|{serial_number:<3} | ", end='')
    print(f"{item["id"]:<13} | ", end='')
    print(f"{item["name"]:<20} | ", end='')
    print(f"{item["number"]:<8} | ", end='')
    print(f"{item["price"]:<10,} | ", end='')
    print(f"{total_price:<12,}|")

print("Tổng số lượng sản phẩm trong giỏ hàng:", sum(item["number"] for item  in cart_items ))
print("Tổng giá trị đơn hàng:", sum(item["price"] * item["number"] for item in cart_items))

            
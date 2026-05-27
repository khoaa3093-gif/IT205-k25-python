revenue = 0 
total_revenue = 0
target_revenue = 0

for i in range (1, 8):
    revenue = int(input(f"Nhập doanh thu ngày {i}: "))

    total_revenue += revenue
    if revenue >= 5000000 : 
        target_revenue += 1

ave_revenue = total_revenue / 7
print("Tổng doanh thu: ", total_revenue)
print("Doanh thu trung bình hàng ngày: ", ave_revenue)
print("Số ngày đạt doanh thu mục tiêu: ", target_revenue)
# Bài 1: Làm quen với Biến và In thông tin (Khái niệm cơ bản)

# 1. Khai báo các biến (giống như gán giá trị biến rchannel trong Asterisk)
caller_id = "0901234567"      # str (Chuỗi ký tự số)
extension = "101"             # str
duration = 125                # int (Thời lượng gọi tính bằng giây)
price_per_minute = 900.5      # float (Cước phí mỗi phút)
is_answered = True            # bool (Cuộc gọi có được bốc máy không?)

# 2. Lệnh print() dùng để in ra kết quả trên màn hình Terminal
print("=== THÔNG TIN CUỘC GỌI ===")
print("Số gọi đến:", caller_id)
print("Số máy nhánh nhận:", extension)
print("Thời gian đàm thoại (giây):", duration)
print("Trạng thái bốc máy:", is_answered)

# 3. Làm phép toán đơn giản: Tính số phút gọi (chia lấy phần nguyên)
# Trong Python: phép chia // là chia lấy phần nguyên, phép chia / là chia ra số thập phân
minutes = duration // 60
seconds = duration % 60  # Phép chia % là lấy phần dư

print("---")
print("Thời gian quy đổi:", minutes, "phút và", seconds, "giây")

# 4. Tính toán tiền cước (Làm tròn lên mỗi block 1 phút nếu có giây dư)
if seconds > 0:
    billed_minutes = minutes + 1
else:
    billed_minutes = minutes

total_cost = billed_minutes * price_per_minute

print("Tổng số phút tính cước:", billed_minutes)
print("Tổng tiền cước:", total_cost, "VNĐ")

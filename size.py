try:
    big_list = [0] * (10**9)  # 1 พันล้านรายการ
    print("สร้าง list สำเร็จ")
except MemoryError:
    print("หน่วยความจำไม่พอ")

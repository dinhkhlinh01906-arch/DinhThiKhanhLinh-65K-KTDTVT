import tkinter as tk
from tkinter import messagebox

def BSearch(a, x, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if a[mid] == x:
        return mid
    
    if a[mid] > x:
        return BSearch(a, x, left, mid - 1)
    
    return BSearch(a, x, mid + 1, right)

def thuc_hien_tim_kiem():
    try:
        chuoi_mang = entry_mang.get()
        mang_so = [int(i) for i in chuoi_mang.split()]
     
        x = int(entry_x.get())

        vi_tri = BSearch(mang_so, x, 0, len(mang_so) - 1)
        
        if vi_tri != -1:
            label_ket_qua.config(text=f"Kết quả: Tìm thấy tại a[{vi_tri}]", fg="blue")
        else:
            label_ket_qua.config(text="Kết quả: Không tìm thấy số này", fg="red")
            
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số nguyên và cách nhau bằng dấu cách!")

linh = tk.Tk()
linh.title("Chương trình Tìm kiếm nhị phân - Bài 149")
linh.geometry("400x300")

tk.Label(linh, text="TÌM KIẾM NHỊ PHÂN", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(linh, text="Nhập mảng (ví dụ: 2 3 4 5 6 7):").pack()
entry_mang = tk.Entry(linh, width=40)
entry_mang.pack(pady=5)

tk.Label(linh, text="Nhập số x cần tìm:").pack()
entry_x = tk.Entry(linh, width=10)
entry_x.pack(pady=5)

btn_tim = tk.Button(linh, text="Bắt đầu tìm", command=thuc_hien_tim_kiem, bg="lightgray")
btn_tim.pack(pady=15)

label_ket_qua = tk.Label(linh, text="Kết quả sẽ hiển thị ở đây", font=("Arial", 11, "italic"))
label_ket_qua.pack(pady=10)

linh.mainloop()
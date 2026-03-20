import tkinter as tk
from tkinter import messagebox

# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(m):
    if m < 2: return False
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True

# Hàm xử lý khi nhấn nút
def thuc_hien_in():
    try:
        n = int(entry_n.get()) # Lấy n từ ô nhập
        if n <= 0:
            messagebox.showwarning("Chú ý", "Vui lòng nhập n > 0")
            return
            
        danh_sach = []
        so_dang_xet = 2
        
        # Vòng lặp tìm cho đủ n số
        while len(danh_sach) < n:
            if la_so_nguyen_to(so_dang_xet):
                danh_sach.append(str(so_dang_xet))
            so_dang_xet += 1
            
        # Hiển thị kết quả lên khung Text
        txt_ket_qua.config(state="normal") # Mở khóa để ghi chữ
        txt_ket_qua.delete("1.0", tk.END)  # Xóa nội dung cũ
        txt_ket_qua.insert(tk.END, " ".join(danh_sach)) # Ghi danh sách mới
        txt_ket_qua.config(state="disabled") # Khóa lại để người dùng không xóa nhầm
        
    except ValueError:
        messagebox.showerror("Lỗi", "Bạn phải nhập một số nguyên!")

# --- Thiết lập Giao diện ---
root = tk.Tk()
root.title("Tìm n Số Nguyên Tố")
root.geometry("450x350")

tk.Label(root, text="Nhập số lượng (n):", font=("Arial", 11)).pack(pady=10)
entry_n = tk.Entry(root, font=("Arial", 12), width=10)
entry_n.pack()

btn_chay = tk.Button(root, text="In kết quả", command=thuc_hien_in, 
                     bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_chay.pack(pady=15)

tk.Label(root, text="Kết quả:").pack()
# Dùng khung Text để hiển thị được nhiều dòng và có thể cuộn
txt_ket_qua = tk.Text(root, height=8, width=50, state="disabled", font=("Consolas", 10))
txt_ket_qua.pack(pady=5, padx=10)

root.mainloop()
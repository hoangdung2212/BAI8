print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
import tkinter as tk

def create_form():
  
    root = tk.Tk()
    root.title("Thông tin cá nhân")

    tk.Label(root, text="Họ tên:").grid(row=0, column=0, padx=10, pady=5)
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Ngày tháng năm sinh:").grid(row=1, column=0, padx=10, pady=5)
    entry_dob = tk.Entry(root)
    entry_dob.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="MSSV:").grid(row=2, column=0, padx=10, pady=5)
    entry_mssv = tk.Entry(root)
    entry_mssv.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Ngành học:").grid(row=3, column=0, padx=10, pady=5)
    entry_major = tk.Entry(root)
    entry_major.grid(row=3, column=1, padx=10, pady=5)

    root.mainloop()

create_form()


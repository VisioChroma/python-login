import tkinter as tk
from tkinter import messagebox
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Registration successful!\nName: {name}\nEmail: {email}")
root = tk.Tk()
root.title("Registration Form")
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root, show="*")  # 'show' hides the password input
entry_password.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Submit", command=submit_form).grid(row=3, column=0, columnspan=2, pady=10)
root.mainloop()
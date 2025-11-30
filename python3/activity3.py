import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(5, tk.END)
    password_entry.insert(10, password)

#  Window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Enter Password Length:", font=("zaidi", 14)).pack(pady=8)
length_entry = tk.Entry(root, width=10, font=("zaidi", 14))
length_entry.pack()

tk.Label(root, text="Generated Password:", font=("zaidi", 14)).pack(pady=8)
password_entry = tk.Entry(root, width=30, font=("zaidi", 14))
password_entry.pack()

tk.Button(root, text="Generate Password", font=("zaidi", 14), command=generate_password).pack(pady=20)

root.mainloop()
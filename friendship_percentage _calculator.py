import tkinter as tk
from tkinter import messagebox
import random

def calculate_friendship():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    if not name1 or not name2:
        messagebox.showerror("Input Error", "Please enter both names!")
        return

    percentage = random.randint(50, 100)

    if percentage > 90:
        msg = "Best friends forever! 💯"
    elif percentage > 75:
        msg = "Great friendship! 🧡"
    elif percentage > 60:
        msg = "Good bond! 😊"
    else:
        msg = "Try to know each other more! 🤗"

    result_label.config(text=f"{name1} 💖 {name2}\nFriendship Score: {percentage}%\n{msg}")

window = tk.Tk()
window.title("Friendship Calculator")
window.geometry("700x500")
window.config(bg="#FFF0F5")

l1 = tk.Label(window,
                  text="🤝 Friendship Percentage Calculator 🤝",
                  font=("Arial", 24, "bold"),
                   bg="#FFF0F5")
l1.pack(pady=10)


l2 = tk.Label(window,
              text = "Your Name:",
              font = ("Arial", 20, "bold"),
                bg="#FFF0F5")
l2.pack()

entry_name1 = tk.Entry(window, 
                       font = ("Arial", 20, "bold"),
                       width=30)
entry_name1.pack(pady=5)

l3 = tk.Label(window,
         text = "Friend's Name:",
          font = ("Arial", 20, "bold"),
           bg="#FFF0F5")
l3.pack()

entry_name2 = tk.Entry(window,
                       font = ("Arial", 20, "bold"),
                       width=30)
entry_name2.pack(pady=5)

b1 = tk.Button(window,
          text = "Calculate Friendship",
           font = ("Arial", 20, "bold"),
            command=calculate_friendship, 
            bg="#FF69B4", fg="white")
b1.pack(pady=10)


result_label = tk.Label(window, 
                        text = "",
                        font=("Arial", 20, "bold"),
                        bg="#FFF0F5")
result_label.pack(pady=10)

window.mainloop()

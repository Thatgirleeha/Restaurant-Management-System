import tkinter as tk
from tkinter import messagebox
from pathlib import Path
root = tk.Tk()
root.title("Resty's Restaurant")
root.geometry("720x520")
root.configure(bg="yellow")
menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soda": 1.99
}
order = {}
photos = {}
def update_order():
    order_box.delete(0, tk.END)
    for food,qty in order.items():
        order_box.insert(tk.END, f"{food} x {qty} - ${menu[food] * qty:.2f}")
    total = sum(menu[food] * qty for food, qty in order.items())
    total_label.config(text=f"Total: ${total:.2f}")
def add(food):
    order[food] = order.get(food, 0) + 1
    update_order()
def remove(food):
    selected = order_box.curselection()
    if selected:
        food = list(order)[selected[0]]
        order[food] -= 1
        if order[food] == 0:
            del order[food]
            update_order()
def checkout():
    if not order:
        messagebox.showinfo("Checkout", "Your order is empty!")
        return
    total = sum(menu[food] * qty for food, qty in order.items())
    messagebox.showinfo("Checkout", f"Your total is ${total:.2f}. Thank you for your order!")
    order.clear()
    update_order()

tk.Label(root, text="Resty's Restaurant", font=("Helvetica", 25), bg="yellow").pack(pady=10)
main = tk.Frame(root, bg="yellow")
main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
left = tk.Frame(main, bg="yellow")
left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right = tk.Frame(main, bg="yellow")
right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
tk.Label(left, text="Menu", font=("Helvetica", 25), bg="yellow").pack(pady=10)
items = tk.Frame(left, bg="yellow")
items.pack()
for food, price in menu.items():
    card = tk.Frame(items, bg="white", bd=2, relief=tk.RIDGE, padx=10, pady=10)
    card.pack(pady=5, fill=tk.X)
    file = Path(__file__).parent / f"{food.lower()}.png"
    if file.exists():
        photos[food] = tk.PhotoImage(file=file)
        tk.Label(card, image=photos[food], bg="white").pack(side=tk.LEFT, padx=10)
    tk.Label(card, text=f"{food} - ${price:.2f}", font=("Helvetica", 15), bg="white").pack(side=tk.LEFT, padx=10)
    tk.Button(card, text="Add", command=lambda f=food: add(f)).pack(side=tk.RIGHT, padx=10)
tk.Label(right, text="Your Order", font=("Helvetica", 25), bg="yellow").pack(pady=10)
order_box = tk.Listbox(right, font=("Helvetica", 15), bg="white")
order_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
total_label=tk.Label(right, text="Total: $0.00", font=("Helvetica", 15), bg="yellow")
total_label.pack(pady=10)
tk.Button(right, text="Remove Selected", command=lambda: remove(order_box.get(order_box.curselection())), bg="red", fg="white").pack(pady=5)
tk.Button(right, text="Place Order", command=checkout, bg="green", fg="white").pack(pady=5)
root.mainloop()
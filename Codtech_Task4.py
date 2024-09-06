import tkinter as tk
from tkinter import messagebox

class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.items = {}

        self.title_label = tk.Label(root, text="Title")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        self.author_label = tk.Label(root, text="Author")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)

        self.type_label = tk.Label(root, text="Type (Book/DVD)")
        self.type_label.grid(row=2, column=0)
        self.type_entry = tk.Entry(root)
        self.type_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0)

        self.checkout_button = tk.Button(root, text="Checkout Item", command=self.checkout_item)
        self.checkout_button.grid(row=3, column=1)

        self.return_button = tk.Button(root, text="Return Item", command=self.return_item)
        self.return_button.grid(row=4, column=0)

        self.search_button = tk.Button(root, text="Search Item", command=self.search_item)
        self.search_button.grid(row=4, column=1)

    def add_item(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        item_type = self.type_entry.get()
        if title and author and item_type:
            self.items[title] = {"author": author, "type": item_type, "available": True}
            messagebox.showinfo("Success", f"Item '{title}' added to the library.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def checkout_item(self):
        title = self.title_entry.get()
        if title in self.items and self.items[title]["available"]:
            self.items[title]["available"] = False
            messagebox.showinfo("Success", f"Item '{title}' checked out.")
        else:
            messagebox.showerror("Error", "Item not available or doesn't exist.")

    def return_item(self):
        title = self.title_entry.get()
        if title in self.items:
            self.items[title]["available"] = True
            messagebox.showinfo("Success", f"Item '{title}' returned.")
        else:
            messagebox.showerror("Error", "Item not found.")

    def search_item(self):
        search_term = self.title_entry.get()
        found_items = [title for title in self.items if search_term.lower() in title.lower()]
        if found_items:
            result = "\n".join(found_items)
            messagebox.showinfo("Search Results", result)
        else:
            messagebox.showerror("Error", "No items found.")

root = tk.Tk()
app = LibraryManagement(root)
root.mainloop()

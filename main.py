import requests
from models.APIResponse import APIResponse
from dataclass_wizard import fromdict
import tkinter as tk
from shutil import which
from tkinter import ttk
from PIL import Image, ImageTk

response = requests.get("https://dummyjson.com/products")
data_dict = response.json()
product_list = fromdict(APIResponse, data_dict)

# for product in product_list.products:
#     print(product.title)
#     print(product.description)
data = response.json()
api_response = 0

def section(product):
    ...

def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.geometry("1200x900")
    root.title("Productos")
    producto = tk.Frame(root)
    producto.pack(side="top")
    for product in product_list.products:
        section(product)
        producto = tk.Frame(root)
        producto.config(width=1100, height=560, border=5)
        producto.pack(side="top")

    root.mainloop()

main()
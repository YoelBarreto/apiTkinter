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

indice = 0
data = response.json()
api_response = 0


tituloL = ""
categoryL = ""
ratingL = ""
precioDiscount = ""
discountL = ""
stockL = ""
descripcionL = ""
dimencionesL = ""
minOrderL = ""
skuL = ""


def cargar():
    global indice, tituloL, categoryL, ratingL, precioDiscount, discountL, stockL, descripcionL, dimencionesL, minOrderL, skuL
    if indice < len(product_list.products):
        si = 0


def siguienteP():
    global indice
    indice += 1

def main():
    global tituloL, categoryL, ratingL, precioDiscount, discountL, stockL, descripcionL, dimencionesL, minOrderL, skuL
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.geometry("1200x600")
    root.title("Productos")
    producto1 = tk.Frame(root)
    producto1.pack(side="top", fill="x")

    img = tk.Frame(producto1, width=40, height=40)
    img.pack(side="left")


    desc = tk.Frame(producto1)
    desc.pack(side="left", fill="x")

    tituloL = ttk.Label(producto1, text="1", font=("Sans", 15), justify="left")
    tituloL.pack(side="top")
    categoryL = ttk.Label(producto1, text="1", font=("Sans", 10), justify="left")
    categoryL.pack(side="top")
    ratingL = ttk.Label(producto1, text="1", font=("Sans", 10), justify="left")
    ratingL.pack(side="top")
    precioDiscount = ttk.Label(producto1, text="1", font=("Sans", 10), justify="left")
    precioDiscount.pack(side="top")


    producto2 = tk.Frame(root)
    producto2.pack(side="top", fill="x", expand=True)


    siguiente = ttk.Button(text="Siguiente", command=siguienteP(), padding=10)
    siguiente.pack()

    cargar()

    root.mainloop()

main()
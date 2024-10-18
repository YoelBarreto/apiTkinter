import requests
from PIL.ImageOps import expand

from models.APIResponse import APIResponse
from dataclass_wizard import fromdict
import tkinter as tk
from textwrap import wrap
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

# product_list.products[indice].id

imagenL = ""
tituloL = ""
categoryL = ""
ratingL = ""
precioDiscount = ""
stockL = ""
descripcionL = ""
dimencionesL = ""
minOrderL = ""
skuL = ""


def cargar():
    global indice, imagenL, tituloL, categoryL, ratingL, precioDiscount, stockL, descripcionL, dimencionesL, minOrderL, skuL
    if indice < len(product_list.products):

        bits_imagen = requests.get(product_list.products[indice].thumbnail, stream=True)
        imagen = Image.open(bits_imagen.raw)
        imagen_tk = ImageTk.PhotoImage(imagen)
        imagenL.config(image=imagen_tk)
        imagenL.image = imagen_tk

        tituloL.config(text=product_list.products[indice].title)
        categoryL.config(text=f"Categoria: #{product_list.products[indice].category}")
        ratingL.config(text=f"Rating: {product_list.products[indice].rating}/5")
        precioDiscount.config(text=f"{product_list.products[indice].price}, (Discount: {product_list.products[indice].discountPercentage})")
        stockL.config(text=f"Stock: {product_list.products[indice].stock}")

        descWrapped = wrap(product_list.products[indice].description, width=130)
        desc = ""
        for line in descWrapped:
            desc += line + "\n"
        descripcionL.config(text=desc)
        dimencionesL.config(text=f"Dimenciones: {product_list.products[indice].dimensions.width} / {product_list.products[indice].dimensions.height} / {product_list.products[indice].dimensions.depth}")
        minOrderL.config(text=f"Minimum Order: {product_list.products[indice].minimumOrderQuantity}")
        skuL.config(text=f"#{product_list.products[indice].sku}")



def siguienteP():
    global indice
    indice += 1
    if indice < len(product_list.products):
        cargar()
    else:
        indice = -1

def main():
    global imagenL, tituloL, categoryL, ratingL, precioDiscount, stockL, descripcionL, dimencionesL, minOrderL, skuL
    # Pantalla
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.geometry("900x600")
    root.title("Productos")
    #Frame 1/2
    producto1 = tk.Frame(root, height=300)
    producto1.pack(side="top", fill="x", expand=True)

    #Frame 1.5/2
    img = tk.Frame(producto1, width=200, height=200)
    img.pack(side="left")

    imagenL = ttk.Label(img, text="loading...", width=200)
    imagenL.pack(fill="both", expand=True)


    #Frame 2.0/0
    desc = tk.Frame(producto1)
    desc.pack(side="left", fill="x")

    tituloL = ttk.Label(producto1, text="1", font=("Sans", 25), justify="left")
    tituloL.pack(side="top", anchor="w")
    categoryL = ttk.Label(producto1, text="1", font=("Sans", 20), justify="left")
    categoryL.pack(side="top", anchor="w")
    ratingL = ttk.Label(producto1, text="1", font=("Sans", 20), justify="left")
    ratingL.pack(side="top", anchor="w")
    precioDiscount = ttk.Label(producto1, text="1", font=("Sans", 20), justify="left")
    precioDiscount.pack(side="top", anchor="w")

    #Frame 2/2
    producto2 = tk.Frame(root)
    producto2.pack(side="top", fill="both", expand=True)

    stockL = ttk.Label(producto2, text="1", font=("Sans", 10), justify="left")
    stockL.pack(side="top", anchor="w")
    descripcionL = ttk.Label(producto2, text="1", font=("Sans", 10), justify="left")
    descripcionL.pack(side="top", anchor="w")
    dimencionesL = ttk.Label(producto2, text="1", font=("Sans", 10), justify="left")
    dimencionesL.pack(side="top", anchor="w")
    minOrderL = ttk.Label(producto2, text="1", font=("Sans", 10), justify="left")
    minOrderL.pack(side="top", anchor="w")
    skuL = ttk.Label(producto2, text="1", font=("Sans", 30), justify="left")
    skuL.pack(side="top", anchor="w")

    siguiente = ttk.Button(text="Siguiente", command=siguienteP, padding=10)
    siguiente.pack()

    cargar()

    root.mainloop()

main()
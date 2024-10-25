import requests
from PIL.ImageOps import expand

from models.APIResponse import APIResponse
from dataclass_wizard import fromdict
import tkinter as tk
from textwrap import wrap
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as alert

# Funcionamiento del response de la API
response = requests.get("https://dummyjson.com/products")
data_dict = response.json()
product_list = fromdict(APIResponse, data_dict)
data = response.json()
api_response = 0

# Creación del indice en el primer valor del elemento al iniciar el programa
indice = 0
lista_resultados = []
background = "#7ec4ff"

# (TEMPORAL) guia del uso del APIresponse
# for product in product_list.products:
#     print(product.title)
#     print(product.description)

# product_list.products[indice].id

# Pantalla de carga de la pantalla principal por indices
def cargar():
    global indice, imagenL, tituloL, categoryL, ratingL, precioDiscount, stockL, descripcionL, dimencionesL, minOrderL, skuL, buscador, buscar
    if indice < len(product_list.products):

        bits_imagen = requests.get(product_list.products[indice].thumbnail, stream=True)
        imagen = Image.open(bits_imagen.raw)
        imagen_tk = ImageTk.PhotoImage(imagen)
        imagenL.config(image=imagen_tk)
        imagenL.image = imagen_tk

        tituloL.config(text=product_list.products[indice].title)
        categoryL.config(text=f"Category: #{product_list.products[indice].category}")
        ratingL.config(text=f"Rating: {product_list.products[indice].rating}/5")
        precioDiscount.config(text=f"{product_list.products[indice].price}, (Discount: {product_list.products[indice].discountPercentage})")
        stockL.config(text=f"Stock: {product_list.products[indice].stock}")

        descWrapped = wrap(product_list.products[indice].description, width=90)
        desc = ""
        for line in descWrapped:
            desc += line + "\n"
        descripcionL.config(text=desc)
        dimencionesL.config(text=f"Dimensions: {product_list.products[indice].dimensions.width} / {product_list.products[indice].dimensions.height} / {product_list.products[indice].dimensions.depth}")
        minOrderL.config(text=f"Minimum Order: {product_list.products[indice].minimumOrderQuantity}")
        skuL.config(text=f"#{product_list.products[indice].sku}")

# def generar_pdf(productos: List[Product]):
#     empresa: Empresa = Empresa(
#         nombre="Alvarikola Soft S.L",
#         titular="Añvarotinga",
#         cif="A12378712F",
#         direccion="Calle Bobo",
#         email="holabobo.dev"
#     )
#     # GENERO PDF (nombre=busqueda_resultado_202410241345.pdf
#     alert.showinfo("PDF Generado", "Se ha generado el PDF correctamente en la ruta /pdfs")

def listaResultados():
    global lista_resultados

    pantalla_resultados = tk.Tk()
    pantalla_resultados.configure(bg=background)
    pantalla_resultados.title("Listado")

    titulo = ttk.Label(pantalla_resultados, text="Productos encontrados", font=("Sans", 20, "bold"))
    titulo.pack

    lista_resultados.sort()
    for resultado in lista_resultados:
        listado = ttk.Label(pantalla_resultados, text=str(resultado))
        listado.configure(background=background)
        listado.pack()
    generarpdf = ttk.Button(pantalla_resultados, text="Generar PDF")
    generarpdf.pack(pady=10)

# Funcionamiento de la busqueda de los productos
def buscarP():
    global buscador, lista_resultados
    texto = buscador.get().lower()
    for i in range(len(product_list.products)):
        if texto in product_list.products[i].title.lower():
            lista_resultados.append(product_list.products[i].title)

    listaResultados()


#Boton de avanzar el producto de la pantalla principal
def siguienteP():
    global indice, contador
    print(indice)
    indice += 1
    if indice < len(product_list.products):
        cargar()
    else:
        indice = -1

#Boton de regresar el producto de la pantalla principal
def volverP():
    global indice
    print(indice)
    indice -= 1
    if indice < len(product_list.products):
        cargar()
    else:
        indice = len(product_list.products) - 1

# Creador de pantalla principal
def main():
    global imagenL, tituloL, categoryL, ratingL, precioDiscount, stockL, descripcionL, dimencionesL, minOrderL, skuL, buscador, buscar
    # Pantalla
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.configure(bg=background)
    root.geometry("900x700")
    root.title("Productos")

    #Buscador
    buscador = ttk.Entry(width=35)
    buscador.pack(pady=15)
    buscar = ttk.Button(text="Buscar", command=buscarP)
    buscar.pack()

    #Frame 1/2
    producto1 = tk.Frame(root, height=300)
    producto1.configure(bg=background)
    producto1.pack(side="top", fill="x", expand=True)

    #Frame 1.5/2
    img = tk.Frame(producto1, width=200, height=200)
    img.configure(bg=background)
    img.pack(side="left")

    imagenL = ttk.Label(img, text="loading...", width=200, borderwidth=2, relief="solid")
    imagenL.configure(background="#9ed2ff")
    imagenL.pack(fill="both", expand=True)


    #Frame 2.0/0
    desc = tk.Frame(producto1)
    desc.configure(bg=background)
    desc.pack(side="left", fill="x")

    tituloL = ttk.Label(producto1, text="1", font=("Sans", 25, "bold"), justify="left")
    tituloL.configure(background=background)
    tituloL.pack(side="top", anchor="w")
    categoryL = ttk.Label(producto1, text="1", font=("Sans", 20), justify="left")
    categoryL.configure(background=background)
    categoryL.pack(side="top", anchor="w")
    ratingL = ttk.Label(producto1, text="1", font=("Sans", 22), justify="left")
    ratingL.configure(background=background)
    ratingL.pack(side="top", anchor="w")
    precioDiscount = ttk.Label(producto1, text="1", font=("Sans", 20, "bold"), justify="left")
    precioDiscount.configure(background=background, foreground="red")
    precioDiscount.pack(side="top", anchor="w")
    stockL = ttk.Label(producto1, text="1", font=("Sans", 20, "bold"), justify="left")
    stockL.configure(background=background, foreground="#e48400")

    #Frame 2/2
    producto2 = tk.Frame(root)
    producto2.configure(bg=background)
    producto2.pack(side="top", fill="both", expand=True)

    stockL.pack(side="top", anchor="w")
    descripcionL = ttk.Label(producto2, text="1", font=("Sans", 15), justify="left")
    descripcionL.configure(background=background)
    descripcionL.pack(side="top", anchor="w")
    dimencionesL = ttk.Label(producto2, text="1", font=("Sans", 15), justify="left")
    dimencionesL.configure(background=background)
    dimencionesL.pack(side="top", anchor="w")
    minOrderL = ttk.Label(producto2, text="1", font=("Sans", 15), justify="left")
    minOrderL.configure(background=background)
    minOrderL.pack(side="top", anchor="w")
    skuL = ttk.Label(producto2, text="1", font=("Sans", 13, "bold"), justify="left")
    skuL.configure(background=background)
    skuL.pack(side="top", anchor="w")

    atras = ttk.Button(root, text="Volver", command=volverP, padding=10)
    atras.pack(ipadx=20)
    siguiente = ttk.Button(root, text="Siguiente", command=siguienteP, padding=10)
    siguiente.pack(ipadx=20)

    cargar()

    root.mainloop()

main()
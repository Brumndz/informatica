import tkinter as tk
from PIL import Image, ImageTk   # You need pillow installed

ventana = tk.Tk()
ventana.title("Acerca de Windows")

# ---- Load Image ----
img = Image.open("win7logo.png")   # put your image file here
img = img.resize((225, 150))   # optional resize
img_tk = ImageTk.PhotoImage(img)

# ---- Frame to hold image + text ----
contenedor = tk.Frame(ventana)
contenedor.pack(pady=20)

# ---- Image Label ----
img_label = tk.Label(contenedor, image=img_tk)
img_label.pack(side="left", padx=10)

# ---- Text Label ----
texto_label = tk.Label(contenedor, text="Windows 7 Ultimate", font=("Segoe UI", 20))
texto_label.pack(side="left", padx=10)

ventana.mainloop()

import tkinter as tk
ventana = tk.Tk()
ventana.geometry("200x300")
ventana.config(bg="green")
ventana.title("Acerca de Windows")

mensaje = tk.Label(ventana,text= "Windows 7 Ultimate ", font=("Segoe UI",20))
mensaje.pack(pady=20)
mensaje.config(bg="lightgreen")
ventana.mainloop()
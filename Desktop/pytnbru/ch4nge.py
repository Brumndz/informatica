import os
import shutil

carpeta = os.path.join(os.path.expanduser("~"), r"C:\Users\Daniel\CARPETASA")

tipos = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Música": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Comprimidos": [".zip", ".rar", ".tar", ".gz"],
    "Programas": [".exe", ".msi", ".deb", ".AppImage", ".sh"],
}

for carpeta_tipo in tipos.keys():
    os.makedirs(os.path.join(carpeta, carpeta_tipo), exist_ok=True)

for archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta_archivo):
        extension = os.path.splitext(archivo)[1].lower()
        for tipo, extensiones in tipos.items():
            if extension in extensiones:
                destino = os.path.join(carpeta, tipo, archivo)
                shutil.move(ruta_archivo, destino)
                print(f"Movido: {archivo} → {tipo}")
                break

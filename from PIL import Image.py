from PIL import Image

# Abrir la imagen
image = Image.open("/Users/HP/Desktop/Diploma_Grado.jpg")

# Crear un archivo PDF vacío
pdf_file = open("Diploma_Grado.pdf", "wb")

# Escribir la imagen en el archivo PDF
image.save(pdf_file, "PDF")

# Cerrar el archivo PDF
pdf_file.close()
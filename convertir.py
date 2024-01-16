import os
import sys

from PIL import Image

ruta_actual = os.getcwd()


def convertir_a_pdf(ruta_imagen:str, nueva_ruta_de_imagen:str):
    """ Convertir una imagen a formato PDF. """
    objeto_imagen = Image.open(ruta_imagen)  # Cargar la imagen
    objeto_imagen.save(nueva_ruta_de_imagen, "PDF", resolution=100.0, save_all=True)  # Convertir la imagen a formato PDF
    print(f"Imagen convertida a formato PDF: {nueva_ruta_de_imagen}")


def existen_archivos(lista_archivos:list[str]):
    """ Devuelve True si todos los archivos especificados existen en la ruta actual. """
    return all(os.path.exists(os.path.join(ruta_actual, archivo)) for archivo in lista_archivos)


def cambiar_formato(tipo_a_convertir:str, imagenes:list[str]):
    """ Cambia el formato de las imágenes especificadas. """
    for imagen in imagenes:
        try:
            ruta_imagen = os.path.join(ruta_actual, imagen)  # Ruta completa de la imagen a convertir
            objeto_imagen = Image.open(ruta_imagen)  # Cargar la imagen

            if tipo_a_convertir == ".jpeg" and objeto_imagen.mode == "P":  # Verificar si la imagen es de paleta
                # Convertir la imagen de paleta (P) a modo RGB si el formato de salida es JPEG
                objeto_imagen = objeto_imagen.convert("RGB")
            
            nuevo_nombre = os.path.splitext(imagen)[0] + f"_Nuevo{tipo_a_convertir}"  # Nuevo nombre de la imagen
            nueva_ruta_de_imagen = os.path.join(ruta_actual, nuevo_nombre)  # Nueva ruta de la imagen

            if tipo_a_convertir == ".pdf":
                convertir_a_pdf(ruta_imagen, nueva_ruta_de_imagen)
            else:
                objeto_imagen.save(nueva_ruta_de_imagen, formato=tipo_a_convertir)
        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")
        else:
            print(f"Se ha convertido {imagen} a {tipo_a_convertir}.")

    print("Cambio")



def main():
    try:
        tipo_a_convertir, *imagenes = sys.argv[1:]
    except:
        print("Debe proporcionar un tipo de imagen a convertir y al menos una imagen.")
        return

    tipo_a_convertir = tipo_a_convertir.lower()

    if len(imagenes) < 1:
        print("Debe proporcionar al menos una imagen a convertir.")
        return

    if not existen_archivos(imagenes):
        print("Uno de los archivos especificados no existe.")
        return
    
    if not tipo_a_convertir.startswith("."):
        tipo_a_convertir = "." + tipo_a_convertir

    if not tipo_a_convertir in (".jpg", ".jpeg", ".png", ".pdf", ".webp", ".bmp", ".gif", ".tiff"):
        print("El tipo a convertir debe ser .jpg, .jpeg, .png, .webp, .bmp, .gif o .tiff.")
        return

    # imagenes_compatibes = all(imagen.lower().endswith(tipo_a_convertir) for imagen in imagenes)
    # if not imagenes_compatibes:
    #     print("Uno de los archivos especificados no es compatible con el tipo a convertir.")
    #     return
    
    cambiar_formato(tipo_a_convertir, imagenes)



if __name__ == "__main__":
    main()

from model.Libros import Libros
import service.file_services as file
import os
from operator import length_hint

# Obtener la ruta al archivo libros.json
__file__= "libros.json"
archivo_json = os.path.abspath(__file__)
rutalibros = file.load_json(archivo_json)

# Función para agregar un libro

def agregar_libro(titulo, autor):
    Libros.id = length_hint(rutalibros)
   
    #input( f"\nPresione ENTER para Continuar..." )
    libro = Libros(titulo, autor)
    libro.description()
    rutalibros.append(libro.__dict__)
    file.write_json(archivo_json, rutalibros )

    print("Libro agregado con éxito.")

# Función para listar todos los libros
def listar_libros():
        print("Lista de libros:\n")
        for i, libro in enumerate(rutalibros):
            exist = True
            print(libro)
        #    print(f"{i}. Título: {libro['Titulo']}, Autor: {libro['Autor']}")
       
        if not exist:
           print("No hay libros en la lista.")

# Función para eliminar un libro
def eliminar_libro(titulo):
    if rutalibros:
        for libro in rutalibros[:]:
            if libro['titulo'] == titulo:
                rutalibros.remove(libro)
                file.write_json(archivo_json, rutalibros)
                print(f"Libro '{titulo}' ha sido eliminado con éxito.")
                return
        print(f"No se encontró un libro con el título '{titulo}' en la lista.")
    else:
        print("No hay libros en la lista.")

# Función para modificar un libro
def modificar_libro( titulo, nuevo_titulo, nuevo_autor):
    if rutalibros:
        for libro in rutalibros:
            if libro['titulo'] == titulo:
                libro['titulo'] = nuevo_titulo
                libro['autor'] = nuevo_autor
                file.write_json(archivo_json, rutalibros)
                print(f"Libro '{titulo}' ha sido modificado a '{nuevo_titulo}' de '{nuevo_autor}'.")
                return
        print(f"No se encontró un libro con el título '{titulo}' en la lista.")
    else:
        print("No hay libros en la lista.")



customer_service = {
    1: agregar_libro,
    2: listar_libros,
    3: modificar_libro,
    4: eliminar_libro,
}

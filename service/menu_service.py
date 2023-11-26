import config.data as data
import helpers.option_helpers as helpers
from service.libros_service import agregar_libro, listar_libros,modificar_libro, eliminar_libro


def menu_service():

   data.selections[0] = helpers.menu(data.options, 'main')
   
   if (data.selections[0] == 1):
          titulo = input("\nIntroduce el título del libro: ")
          autor = input("\nIntroduce el autor del libro: ")
          agregar_libro(titulo, autor)
          input( f"\nPresione ENTER para Continuar..." )

   if (data.selections[0] == 2):
          listar_libros()
          input( f"\nPresione ENTER para Continuar..." )
          print("\n")
   if (data.selections[0] == 3):
          titulo = input("\nIntroduce el título del libro que deseas modificar: ")
          nuevo_titulo = input("\nIntroduce el nuevo título del libro: ")
          nuevo_autor = input("\nIntroduce el nuevo autor del libro: ")
          modificar_libro(titulo, nuevo_titulo, nuevo_autor)
          input( f"\nPresione ENTER para Continuar..." )
          print("\n")
   if (data.selections[0] == 4):
          titulo = input("\nIntroduce el título del libro que deseas eliminar: ")
          eliminar_libro(titulo)
          input( f"\nPresione ENTER para Continuar..." )
          print("\n")


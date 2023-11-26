class Libros:

    id = 0

    def __init__(self, titulo, autor):
        Libros.id += 1
        self.id = Libros.id
        self.titulo = titulo
        self.autor = autor
        
    def description(self):
        print(f"\nLos datos son:\n") 
        print(f"id:{self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
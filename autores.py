class Autor:
    
    def __init__(self):
        pass
    def AgregarAutor(self, nombre, apellido, nacionalidad, codigo):
        self.nombres = nombre
        self.apellidos = apellido
        self.nacionalidad = nacionalidad
        self.codigo = codigo
        self.libros = list()

    def AgregarLibro(self, libro):
        self.libros.append(libro)
    
    def VerLibrosPorAutor(self):
        for book in range(len(self.libros)):
            print(f"{self.libros[book]}")
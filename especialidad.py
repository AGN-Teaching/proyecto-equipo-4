import pickle

# Esta clase se utiliza para administrar especialidades médicas y guardarlas en un archivo.
class Especialidad:
    def __init__(self):
    
        self.__especialidades = []  # Inicializa una lista vacía para almacenar las especialidades.

    # Método para agregar una nueva especialidad médica.
    def agregar_especialidad(self, nombre, descripcion):
      
        # Intentamos cargar las especialidades médicas existentes desde un archivo.
        with open("especialidades_medicas.dat", 'rb') as archivo:
            self.__especialidades = pickle.load(archivo)

        # Agregamos la nueva especialidad a la lista de especialidades.
        self.__especialidades.append((nombre, descripcion))

        # Muestra un mensaje para confirmar que la especialidad ha sido agregada.
        print(f'Especialidad "{nombre}" agregada.')

        # Finalmente, guarda la lista actualizada de especialidades en el archivo.
        with open("especialidades_medicas.dat", 'wb') as archivo:
            pickle.dump(self.__especialidades, archivo)

    # Método para mostrar la lista de especialidades médicas.  
    def mostrar_especialidades(self):
        
        # Carga la lista de especialidades médicas desde el archivo.
        with open("especialidades_medicas.dat", 'rb') as archivo:
            self.__especialidades = pickle.load(archivo)

        # Imprime una lista de las especialidades médicas y sus descripciones.
        print("Lista de especialidades:")
        for especialidad, descripcion in self.__especialidades:
            print(f"Nombre: {especialidad}")
            print(f"Descripción: {descripcion}")
            print("-" * 40)

    # Método para eliminar una especialidad médica según su nombre.
    def borrar_especialidad(self, nombre):

        # Intentamos cargar las especialidades médicas existentes desde un archivo.
        with open("especialidades_medicas.dat", 'rb') as archivo:
            self.__especialidades = pickle.load(archivo)

        # Elimina la especialidad con el nombre proporcionado de la lista de especialidades.
        self.__especialidades = [(especialidad, descripcion) for especialidad, descripcion in self.__especialidades if especialidad.lower() != nombre.lower()]

        # Muestra un mensaje para confirmar que la especialidad ha sido eliminada.
        print(f'Especialidad "{nombre}" eliminada.')

        # Finalmente, guarda la lista actualizada de especialidades en el archivo.
        with open("especialidades_medicas.dat", 'wb') as archivo:
            pickle.dump(self.__especialidades, archivo)

    # Método para obtener una especialidad médica según su nombre.
    def get_especialidad(self, nombre):

        for especialidad, descripcion in self.__especialidades:
            if especialidad.lower() == nombre.lower():
                return (especialidad, descripcion)

        # Si no se encuentra la especialidad, devuelve None.
        return None

    # Método para mostrar solo los nombres de las especialidades médicas.
    def mostrar_especialidades_nombre(self):

        # Carga la lista de especialidades médicas desde el archivo.
        with open("especialidades_medicas.dat", 'rb') as archivo:
            self.__especialidades = pickle.load(archivo)
        
        # Imprime una lista de los nombres de las especialidades médicas.
        print("Lista de especialidades:")
        for especialidad in self.__especialidades:
            print(f"Nombre: {especialidad[0]}")
            print("-" * 40)

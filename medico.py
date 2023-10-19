import pickle

class Medico:
    
    def __init__(self, nombre, cedula_profesional, especialidades, cedulas_especialidad):
        self.__nombre_medico = nombre
        self.__cedula_profesional = cedula_profesional
        self.__especialidades = especialidades
        self.__cedulas_especialidad = cedulas_especialidad

    # Método para obtener una representación en cadena del objeto médico.
    def __str__(self):
        return f"Nombre: {self.__nombre_medico}\nCédula Profesional: {self.__cedula_profesional}\nEspecialidades: {', '.join(self.__especialidades)}\nCédulas de Especialidad: {', '.join(self.__cedulas_especialidad)}"

    # Método para obtener el nombre del médico.
    def get_nombre_medico(self):
        return self.__nombre_medico
    
    # Método para obtener la cédula profesional del médico.
    def get_cedula_profesional(self):
        return self.__cedula_profesional

    # Método estático para eliminar un médico por su cédula profesional.
    @staticmethod
    def eliminar_medico(cedula):
        try:
            # Abre el archivo "medicos.dat" y cargar la lista de médicos.
            with open("medicos.dat", "rb") as archivo:
                medicos_exist = pickle.load(archivo)

            # Elimina el médico con la cédula proporcionada.
            medicos_exist = [medico for medico in medicos_exist if medico._Medico__cedula_profesional != cedula]

            # Guarda la lista actualizada de médicos en el archivo "medicos.dat".
            with open("medicos.dat", "wb") as archivo:
                pickle.dump(medicos_exist, archivo)

            print(f"Médico con cédula {cedula} eliminado exitosamente.")
        except FileNotFoundError:
            print(f"No se encontró el archivo 'medicos.dat'. No se realizó ninguna eliminación.")

    # Método estático para mostrar la lista de médicos.
    @staticmethod
    def mostrar_medicos():
        try:
            # Intenta abrir el archivo "medicos.dat" y cargar la lista de médicos.
            with open("medicos.dat", "rb") as archivo:
                medicos_exist = pickle.load(archivo)
        except FileNotFoundError:
            medicos_exist = []

        # Imprime la lista de médicos y sus detalles.
        print("Lista de médicos:")
        for medico_existente in medicos_exist:
            print(str(medico_existente))
            print("-" * 40)

    # Método estático para mostrar solo los nombres y cédulas de los médicos.
    @staticmethod
    def mostrar_nombres_cedulas():
        try:
            # Intenta abrir el archivo "medicos.dat" y cargar la lista de médicos.
            with open("medicos.dat", "rb") as archivo:
                medicos_exist = pickle.load(archivo)
        except FileNotFoundError:
            medicos_exist = []
            
        # Imprime la lista de médicos con sus nombres y cédulas.
        print("Lista de médicos:")
        for medico_existente in medicos_exist:
            print(f"Nombre: {medico_existente.get_nombre_medico()}, Cédula: {medico_existente.get_cedula_profesional()}")
            print("-" * 40)

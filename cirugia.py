import pickle

# Esta clase representa una cirugía y se utiliza para almacenar información sobre las cirugías programadas.
class Cirugia:
    def __init__(self, nombre_cirugia="", fecha_programada="", cirujano=None, sala_cirugia="", observaciones=""):
       
        # Atributos de la cirugía:
        self.__nombre_cirugia = nombre_cirugia  # El nombre de la cirugía.
        self.__fecha_programada = fecha_programada  # La fecha programada para la cirugía.
        self.__cirujano = cirujano  # El cirujano asignado a la cirugía.
        self.__sala_cirugia = sala_cirugia  # La sala de cirugía donde se llevará a cabo la cirugía.
        self.__observaciones = observaciones  # Cualquier observación o nota relacionada con la cirugía.

        self.__cirugia = []  # Una lista vacía que se utilizará para almacenar información sobre cirugías.

    #Permite obtener una representación en cadena de la instancia cirugía
    def __str__(self):

        # Obtiene el nombre del cirujano.
        cirujano_nombre = self.__cirujano.get_nombre_medico()

        # Crea una cadena con detalles de la cirugía.
        return f"Nombre de la Cirugía: {self.__nombre_cirugia}\nFecha Programada: {self.__fecha_programada}\nNombre del Cirujano: {cirujano_nombre}\nSala de Cirugía: {self.__sala_cirugia}\nObservaciones: {self.__observaciones}"

    # Método para cargar información sobre cirugías desde un archivo binario
    def cargar_cirugias_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as archivo:
                self.__cirugia = pickle.load(archivo)  # Deserializa la información de cirugías desde el archivo y la almacena en la lista de cirugías.
        except FileNotFoundError:
            print("El archivo no existe o no se puede abrir.")
        except Exception as e:
            print(f"Error al cargar cirugías desde el archivo: {str(e)}")

    # Método para buscar cirugías que coincidan con los síntomas proporcionados por un paciente.
    def buscar_cirugia(self, sintomas_paciente):
        
        # Inicializamos una lista vacía para almacenar las cirugías encontradas.
        cirugias_encontradas = []

        # Itera a través de la lista de cirugías.
        for cirugia in self.__cirugia:
            nombre_cirugia, sintomas_cirugia = cirugia
            
            # Comprueba si todos los síntomas del paciente están presentes en la descripción de la cirugía.
            if all(sintoma.lower() in sintomas_cirugia.lower() for sintoma in sintomas_paciente):
                cirugias_encontradas.append((nombre_cirugia, sintomas_cirugia))

        if cirugias_encontradas:
            return cirugias_encontradas  # Devuelve una lista de cirugías que coinciden con los síntomas del paciente.
        else:
            return "No se encontraron cirugías para los síntomas proporcionados por el paciente"  # Devuelve un mensaje si no se encuentran coincidencias.

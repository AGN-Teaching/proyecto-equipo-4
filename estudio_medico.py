import pickle

# Esta clase se utiliza para representar información sobre estudios médicos, como análisis de laboratorio.
class EstudioMedico:
    def __init__(self, tipo_estudio="", fecha_programada="", centro_medico="", instrucciones_previas=""):

        self.__tipo_estudio = tipo_estudio  # Tipo de estudio médico.
        self.__fecha_programada = fecha_programada  # Fecha programada para el estudio.
        self.__centro_medico = centro_medico  # Centro médico donde se realizará el estudio.
        self.__instrucciones_previas = instrucciones_previas  # Instrucciones previas al estudio.

    # Método para obtener una representación en cadena del objeto EstudioMedico.
    def __str__(self):
    
        return f"Informe de Laboratorio para el estudio de {self.__tipo_estudio}\nFecha Programada: {self.__fecha_programada}\nCentro Médico: {self.__centro_medico}\nInstrucciones Previas: {self.__instrucciones_previas}\n"
    
    # Método para cargar información de estudios médicos desde un archivo.
    def cargar_estudios_desde_archivo(self, nombre_archivo):

        with open(nombre_archivo, 'rb') as archivo:
            self._estudios_medicos = pickle.load(archivo)

    # Método para buscar estudios médicos que coincidan con los síntomas proporcionados por el paciente.
    def buscar_estudio_medico(self, sintomas_paciente):

        estudios_encontrados = []
        for nombre, sintomas in self._estudios_medicos:
            # Compara cada síntoma proporcionado por el paciente con los síntomas del estudio médico.
            if all(sintoma.lower() in sintomas.lower() for sintoma in sintomas_paciente):
                estudios_encontrados.append((nombre, sintomas))

        # Si se encuentran estudios médicos que coinciden con los síntomas, se devuelven. 
        # De lo contrario, se devuelve un mensaje indicando que no se encontraron coincidencias.
        if estudios_encontrados:
            return estudios_encontrados
        else:
            return "No se encontraron procedimientos médicos para los síntomas proporcionados por el paciente"

    # Método que busca y muestra estudios médicos que coinciden con un síntoma proporcionado.
    def buscar_y_mostrar_estudio_medico(self, sintoma):

        # Cargamos la información de estudios médicos desde un archivo.
        self.cargar_estudios_desde_archivo("estudios_medicos.dat")

        # Se utiliza el método "buscar_estudio_medico" para buscar estudios que coincidan con el síntoma proporcionado.
        estudios_encontrados = self.buscar_estudio_medico(sintoma)

        # Se devuelve la lista de estudios médicos encontrados.
        return estudios_encontrados

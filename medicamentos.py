import pickle

class Medicamento:
    def _init(self):
        self.__medicamentos = [] #Lista para almacenar los medicamentos

    # Método para agregar un medicamento con nombre, síntomas y dosis a un archivo específico.
    def agregar_medicamento(self, nombre, sintomas, dosis, nombre_archivo):
        
        # Carga la lista de medicamentos desde el archivo.
        with open(nombre_archivo, 'rb') as archivo:
            self.__medicamentos = pickle.load(archivo)
        # Agrega un nuevo medicamento a la lista.
        self.__medicamentos.append((nombre, ', '.join(sintomas), dosis))
        # Guarda la lista actualizada en el archivo.
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(self.__medicamentos, archivo)

    # Método para cargar la lista de medicamentos desde un archivo específico.
    def cargar_medicamentos_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            self.__medicamentos = pickle.load(archivo)

    # Método para buscar y mostrar medicamentos relacionados con un síntoma específico.
    def buscar_y_mostrar_medicamentos(self, sintoma):
        
        # Carga la lista de medicamentos desde el archivo "medicamentos.dat".
        self.cargar_medicamentos_desde_archivo("medicamentos.dat")
        # Llama al método "buscar_medicamentos" para buscar medicamentos relacionados con el síntoma.
        medicamentos_encontrados = self.buscar_medicamentos(sintoma)
        # Devuelve los medicamentos encontrados.
        return medicamentos_encontrados

    # Método para buscar medicamentos que coincidan con una lista de síntomas proporcionada.
    def buscar_medicamentos(self, sintomas_paciente):
        medicamentos_encontrados = []
        for nombre, sintomas, dosis in self.__medicamentos:
            if all(sintoma.lower() in sintomas.lower() for sintoma in sintomas_paciente):
                medicamentos_encontrados.append((nombre, sintomas, dosis))

        # Devuelve la lista de medicamentos encontrados o un mensaje si no se encontraron.
        if medicamentos_encontrados:
            return medicamentos_encontrados
        else:
            return "No se encontraron medicamentos para los síntomas proporcionados por el paciente"

    # Método para eliminar un medicamento por su nombre.
    def eliminar_medicamento(self, nombre):
        with open("medicamentos.dat", 'rb') as archivo:
            self.__medicamentos = pickle.load(archivo)
    # Elimina el medicamento con el nombre proporcionado
        self.__medicamentos = [medicamento for medicamento in self.__medicamentos if medicamento[0].lower() != nombre.lower()]
        # Guarda la lista actualizada de medicamentos en el archivo "medicamentos.dat".
        with open("medicamentos.dat", 'wb') as archivo:
            pickle.dump(self.__medicamentos, archivo)

        print(f'Medicamento "{nombre}" eliminado.')

    # Método para mostrar la lista completa de medicamentos.
    def mostrar_medicamentos(self):
        with open("medicamentos.dat", 'rb') as archivo:
            self.__medicamentos = pickle.load(archivo)
        # Imprime la lista de medicamentos, incluyendo nombre, síntomas y dosis.
        print("Lista de medicamentos:")
        for nombre, sintomas, dosis in self.__medicamentos:
            print(f"Nombre: {nombre}")
            print(f"Síntomas: {sintomas}")
            print(f"Dosis: {dosis}")
            print("-" * 40)

    # Método para mostrar solo los nombres de los medicamentos.
    def mostrar_medicamento_nombre(self):
        with open("medicamentos.dat", 'rb') as archivo:
            self.__medicamentos = pickle.load(archivo)
        # Imprime solo los nombres de los medicamentos.
        print("Lista de medicamentos:")
        for med in self.__medicamentos:
            print(f"Nombre: {med[0]}")
            print("-" * 40)

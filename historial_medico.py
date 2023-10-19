class HistorialMedico:
    def __init__(self, alergias, enfermedades_cronicas, procedimientos_quirurgicos, enfermedades_hereditarias, condiciones_familiares, peso, talla):
        
        self.__alergias = alergias  # Alergias del paciente.
        self.__enfermedades_cronicas = enfermedades_cronicas  # Enfermedades crónicas del paciente.
        self.__procedimientos_quirurgicos = procedimientos_quirurgicos  # Procedimientos quirúrgicos previos del paciente.
        self.__enfermedades_hereditarias = enfermedades_hereditarias  # Enfermedades hereditarias del paciente.
        self.__condiciones_familiares = condiciones_familiares  # Condiciones médicas en la familia del paciente.
        self.__peso = peso  # Peso del paciente.
        self.__talla = talla  # Talla del paciente.

    # Método para obtener una representación en cadena del objeto HistorialMedico.
    def __str__(self):

        return f"Alergias: {self.__alergias}\nEnfermedades Crónicas: {self.__enfermedades_cronicas}\nProcedimientos Quirúrgicos Previos: {self.__procedimientos_quirurgicos}\nEnfermedades Hereditarias: {self.__enfermedades_hereditarias}\nCondiciones Médicas en la Familia: {self.__condiciones_familiares}"

    # Método para obtener las alergias del paciente.
    def get_alergias(self):

        return self.__alergias

    # Método para obtener el peso del paciente.
    def get_peso(self):

        return self.__peso
    
    # Método para obtener la talla del paciente.
    def get_talla(self):

        return self.__talla

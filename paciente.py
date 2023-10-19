class Paciente:
    def __init__(self, nombre, edad, fecha_nacimiento, genero, num_seguro_social, direccion, telefono, correo_electronico, contacto_de_emergencia):

        self.__nombre = nombre
        self.__edad = edad
        self.__fecha_nacimiento = fecha_nacimiento
        self.__genero = genero
        self.__num_seguro_social = num_seguro_social
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo_electronico = correo_electronico
        self.__contacto_emergencia = contacto_de_emergencia

    # Método para obtener una representación en cadena del objeto Paciente.
    def __str__(self):
        
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nFecha de Nacimiento: {self.__fecha_nacimiento}\nGénero: {self.__genero}\nNúmero de Seguro Social: {self.__num_seguro_social}\nDirección: {self.__direccion}\nTeléfono: {self.__telefono}\nCorreo Electrónico: {self.__correo_electronico}\nContacto de Emergencia: {self.__contacto_emergencia}"

    # Método para obtener la edad del paciente.
    def get_edad_paciente(self):

        return self.__edad

    # Método para obtener el nombre del paciente.
    def get_nombre_paciente(self):
       
        return self.__nombre
    
     # Método para obtener el género del paciente.
    def get_genero(self):

        return self.__genero

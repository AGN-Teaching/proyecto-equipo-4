from paciente import Paciente
from receta import Receta
from medico import Medico
from especialidad import Especialidad
from expediente_clinico import ExpedienteClinico
from historial_medico import HistorialMedico
import pickle
import os
import platform
from historial_vacunas import HistorialVacunas
from medicamentos import Medicamento
import pyautogui #Para instalar ingresa en la terminal: pip install pyautogui 
import datetime

class Clinica:
    def __init__(self):
        # Inicialización de la clase Clinica
        # Cargamos los expedientes clínicos
        self.__expedientes_clinico = self.cargar_expedientes()
        
        # Cargamos la información de los médicos
        self.__medicos = self.cargar_medicos()
        
        # Cargamos la información de los medicamentos
        self.__medicamento = self.cargar_medicamentos()
        
        # Cargamos la información de las especialidades médicas
        self.__especialidad = self.cargar_especialidades()
        
        # Creación de una instancia de la clase Especialidad
        self.__especialidades = Especialidad()
        
        # Creación de una instancia de la clase Medico con valores iniciales nulos
        self.__lista_medicos = Medico(nombre=None, cedula_profesional=None, especialidades=None, cedulas_especialidad=None)
        
        # Creación de una instancia de la clase Medicamento
        self.__medicamentos = Medicamento()

    #Este metodo es para borra pantalla, le añadimos una condicional
    #Por si el sistema es windows o mac o linux 
    def borrar(self):
        if platform.system() == "Windows":
            os.system("cls")
            pyautogui.hotkey("ctrl", "l")
        else:
            os.system("clear")
            pyautogui.hotkey("command", "k")
            pyautogui.hotkey("command", "l")

    #Metodo para pausar el programa
    def pausa(self):
        input("Presione Enter para continuar...")

    #Carga a todos los medicamentos que contenga el archivo 
    def cargar_medicamentos(self):
        # Lista para almacenar los medicamentos
        medicamentos = []
        
        # EL archivo donde se almacenarán los medicamentos
        archivo_medicamentos = "medicamentos.dat"

        # Verifica si el archivo de medicamentos existe
        if os.path.exists(archivo_medicamentos):
            # Si el archivo existe, lo abre en modo lectura binaria ("rb")
            with open(archivo_medicamentos, "rb") as archivo:
                # Carga los medicamentos desde el archivo utilizando pickle
                medicamentos = pickle.load(archivo)

        # Retorna la lista de medicamentos
        return medicamentos

    #Caraga a todas las especialidades que contenga el archivo
    def cargar_especialidades(self):
        # lista para almacenar las especialidades médicas
        especialidades = []
        
        # El archivo donde se almacenarán las especialidades médicas
        archivo_especialidades = "especialidades_medicas.dat"

        # Verifica si el archivo de especialidades médicas existe
        if os.path.exists(archivo_especialidades):
            # Si el archivo existe, lo abre en modo lectura binaria ("rb")
            with open(archivo_especialidades, "rb") as archivo:
                # Carga las especialidades médicas desde el archivo utilizando pickle
                especialidades = pickle.load(archivo)

        # Retorna la lista de especialidades médicas 
        return especialidades

    #Caraga a todos los expedientes que contenga el archivo
    def cargar_expedientes(self):
        # lista para almacenar los expedientes clínicos
        expedientes = []
        
        # Itera a través de los archivos en el directorio actual
        for filename in os.listdir():
            # Comprueba si el nombre del archivo termina con "_expediente.dat"
            if filename.endswith("_expediente.dat"):
                # Abre el archivo en modo lectura binaria ("rb")
                with open(filename, "rb") as archivo:
                    # Carga el expediente clínico desde el archivo utilizando pickle
                    expediente = pickle.load(archivo)
                    # Agrega el expediente a la lista de expedientes
                    expedientes.append(expediente)

        # Retorna la lista de expedientes clínicos
        return expedientes

    #Caraga a todos los medicos que contenga el archivo
    def cargar_medicos(self):
        # lista para almacenar la información de médicos
        medicos = []
        
        # El archivo donde se almacenará la información de médicos
        archivo_medicos = "medicos.dat"

        # Verifica si el archivo de información de médicos existe 
        if os.path.exists(archivo_medicos):
            # Si el archivo existe, lo abre en modo lectura binaria ("rb")
            with open(archivo_medicos, "rb") as archivo:
                # Carga la información de médicos desde el archivo utilizando pickle
                medicos = pickle.load(archivo)

        # Retorna la lista de información de médicos 
        return medicos


#Es un metodo que muestra un menú principal en un bucle infinito, permitiendo al usuario seleccionar entre 
#las opciones de "Administrador de sistema," "Médico," "Paciente," o "Salir." Dependiendo de la opción seleccionada, 
#El metodo llama a otros metodos de menú específicas y, en el caso de "Salir," termina el programa.
# También maneja las opciones no válidas con un mensaje de advertencia.
    def menu_principal(self):
        
        while True:
            self.borrar()
            print("---- Menú Principal ----")
            print("1. Administrador de sistema")
            print("2. Médico")
            print("3. Paciente")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.borrar()
                self.menu_administrador()

            elif opcion == "2":
                self.borrar()
                self.menu_medico()
                self.pausa()
            elif opcion == "3":
                self.borrar()
                self.menu_paciente()
                self.pausa()
            elif opcion == "4":
                print("¡Hasta luego!")
                exit()

            else:
                print("Opción no válida. Intente de nuevo.")

#Este método representa el menú específico para administradores en un bucle infinito.
#Permite al administrador seleccionar entre varias opciones, como eliminar pacientes, médicos,
#medicamentos, especialidades, agregar especialidades y medicamentos, mostrar listas de medicamentos, 
#especialidades y médicos, y consultar expedientes. Dependiendo de la opción seleccionada, 
#el método llama a los métodos correspondientes para realizar las tareas deseadas. También maneja las opciones 
#no válidas con un mensaje de advertencia y ofrece la opción de regresar al menú principal.
    def menu_administrador(self):
        while True:
            self.borrar()
            print("\n---- Menú Administrador ----")
            print("1. Eliminar Paciente")
            print("2. Eliminar Médico")
            print("3. Eliminar Medicamento")
            print("4. Eliminar Especialidad")
            print("5. Agregar Especialidad")
            print("6. Agregar Medicamento")
            print("7. Mostrar Medicamentos disponibles")
            print("8. Mostrar Especialidades disponibles")
            print("9. Mostrar Médicos Registrados")
            print("10. Consultar Expediente ")
            print("11. Regresar")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.borrar()
                nombre = input("Ingresa paciente a eliminar: ")
                self.eliminar_paciente(nombre)
            elif opcion == "2":
                self.borrar()
                self.eliminar_medico()
            elif opcion == "3":
                self.borrar()
                self.eliminar_medicamento()
            elif opcion == "4":
                self.borrar()
                self.eliminar_especialidad()
            elif opcion == "5":
                self.borrar()
                self.agregar_especialidades()
            elif opcion == "6":
                self.borrar()
                self.agregar_medicamento()
            elif opcion == "7":
                self.borrar()
                self.mostrar_medicamentos()    
            elif opcion == "8":
                self.borrar()
                self.mostrar_especialidades()
            elif opcion == "9":
                self.borrar()
                self.mostrar_medicos()
            elif opcion == "10":
                self.borrar()
                self.consultar_expediente_administrador()
            elif opcion == "11":
                self.menu_principal()
            else:
                print("Opción no válida. Intente de nuevo.")
            self.pausa()
            
    #Elimina a un paciente por su nombre       
    def eliminar_paciente(self, nombre):
        # variable que tiene el nombre del archivo
        ruta_archivo = f"{nombre}_expediente.dat"
        
        # Verifica si el archivo del expediente existe
        if os.path.exists(ruta_archivo):
            # Si el archivo existe, lo elimina del sistema de archivos
            os.remove(ruta_archivo)
            print(f"El archivo {ruta_archivo} ha sido eliminado.")
        else:
            # Si el archivo no existe, muestra un mensaje indicando que no se encontró
            print(f"El archivo {ruta_archivo} no existe.")

    #Eliminanos a un medico por su cedula
    def eliminar_medico(self):
        # Mostramos los médicos disponibles
        print("Médicos disponibles:")
        Medico.mostrar_nombres_cedulas()

        # Solicitamos la cédula del médico a eliminar
        cedula = input("Ingresar cédula del médico a eliminar: ")

        # Verificar si la cédula existe antes de eliminar
        medico_existente = False
        for medico in self.__medicos:
            if medico.get_cedula_profesional() == cedula:
                medico_existente = True
                break

        if not medico_existente:
            print(f"\nError: No se encontró un médico con la cédula {cedula}.")
            return

        # Eliminamos el médico
        self.__lista_medicos.eliminar_medico(cedula)

    #Eliminamos un medicamento por su nombre
    def eliminar_medicamento(self):
        # Mostramos medicamentos disponibles
        self.__medicamentos.mostrar_medicamento_nombre()

        # Solicitamos el nombre del medicamento a eliminar
        nombre = input("Ingresar nombre del medicamento a eliminar: ")

        # Verificamos si el medicamento existe antes de eliminar
        medicamento_existente = False
        for medicamento in self.__medicamento:
            if medicamento[0].lower() == nombre.lower():
                medicamento_existente = True
                break

        if not medicamento_existente:
            print(f"\nError: No se encontró un medicamento con el nombre {nombre}.")
            return

        # Eliminamos el medicamento
        self.__medicamentos.eliminar_medicamento(nombre)

    #Eliminamos una especialidad por su nombre
    def eliminar_especialidad(self):
        #creamos una instancia especialidad
        especialidad_borrar = Especialidad()
        especialidad_borrar.mostrar_especialidades_nombre()

        # Solicitamos nombre de la especialidad a eliminar
        nombre = input("Ingresar nombre de la especialidad a eliminar: ")

        # Verificamos si la especialidad existe antes de eliminar
        especialidad_existente = False
        for especialidad in self.__especialidad:
            if especialidad[0].lower() == nombre.lower():
                especialidad_existente = True
                break

        if not especialidad_existente:
            print(f"\nError: No se encontró una especialidad con el nombre {nombre}.")
            return

        # Eliminamos la especialidad
        self.__especialidades.borrar_especialidad(nombre)

    #Agregamos una especialidad con su descripcion
    def agregar_especialidades(self):
        
        nombre=input("Ingresa Especialidad:")
        descripcion=input("Ingresa la descripcion:")
        # Llamamos al método "agregar_especialidad" de la instancia de la clase "Especialidad" 
        # para agregar la nueva especialidad
        self.__especialidades.agregar_especialidad(nombre,descripcion)
 
    #Agregamos un medicamos, con sus sitomas para aliviar y su dosis
    def agregar_medicamento(self):
        
        nombre = input("Ingrese el nombre del medicamento: ")
        
        
        sintomas = input("Ingrese los síntomas para los cuales se receta el medicamento (separados por coma): ").split(',')

        dosis = input("Ingrese la dosis recomendada: ")

        # Llama al método "agregar_medicamento" de la instancia de la clase "Medicamento" para agregar el nuevo medicamento.
         # Además, se especifica el nombre del archivo "medicamentos.dat" donde se almacenará la información.
        self.__medicamentos.agregar_medicamento(nombre, sintomas, dosis, "medicamentos.dat")

        print(f"Medicamento '{nombre}' agregado con éxito.")
    
    #Muestra la lista de medicamentos almacenados
    def mostrar_medicamentos(self):
         # Llama al método "mostrar_medicamentos" de la instancia de la clase "Medicamento"
        self.__medicamentos.mostrar_medicamentos()

    #Muestra la lista de medicos almacenados
    def mostrar_medicos(self):
         # Llama al método "mostrar_medicos" de la instancia de la clase "Medico"
        self.__lista_medicos.mostrar_medicos()

    #Muestra la lista de especialidades almacenados
    def mostrar_especialidades(self):
         # Llama al método "mostrar_especialidades" de la instancia de la clase "Especialidad"
        self.__especialidades.mostrar_especialidades()

    #Nos permite buscar y consultar el expediente clínico de un paciente
    def consultar_expediente_administrador(self):
        # Entramos en un bucle que permite buscar expedientes clínicos de los pacientes.
        while True:
            nombre_paciente = input("Ingresa nombre del paciente a buscar: ")
            paciente = None

            try:
                # Intenta abrir y cargar el archivo del expediente clínico del paciente.
                with open(f"{nombre_paciente}_expediente.dat", "rb") as archivo:
                    expediente = pickle.load(archivo)
                    paciente = expediente.paciente
                    historial_medico = expediente.historial_medico
                    historial_vacunas = expediente.historial_vacunas

                    # Muestra información del expediente clínico.
                    print("Expediente Clínico:")
                    print(paciente)
                    print(historial_medico)
                    print(historial_vacunas)
                break
            except FileNotFoundError:
                # Si no se encuentra el expediente clínico, muestra un mensaje y pregunta si se desea intentar de nuevo.
                print(f"No se encontró un expediente clínico para {nombre_paciente}.")
                respuesta = input("¿Quieres intentar de nuevo? (s/n): ")
                if respuesta.lower() != 's':
                    break

        if paciente:
            #Hacemos uso de excepciones
            try:
                # Intenta abrir y leer el archivo de receta médica del paciente.
                with open(f"{paciente.get_nombre_paciente()}_receta_medica.txt", "r") as archivo:
                    contenido = archivo.read()
                    print(contenido)
            except FileNotFoundError:
                # Si no se encuentra la receta médica, muestra un mensaje correspondiente.
                print(f"No se encontró una receta médica para {paciente.get_nombre_paciente()}.")

    #Permite a los médicos seleccionar entre opciones como registrarse, consultar expedientes médicos 
    #o regresar al menú principal. Dependiendo de la opción seleccionada, el código llama a los métodos 
    #correspondientes para llevar a cabo las tareas deseadas. Además, maneja opciones no válidas y ofrece 
    #la opción de volver al menú principal.
    def menu_medico(self):
        while True:
            self.borrar()
            print("\n---- Menú Médico ----")
            print("1. Registrarse")
            print("2. Consultar expediente")
            print("3. Regresar")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.borrar()
                self.registrarse_medico()
            elif opcion == "2":
                self.borrar()
                self.consultar_expediente_medico()
            elif opcion == "3":
                self.menu_principal()
            else:
                print("Opción no válida. Intente de nuevo.")
            self.pausa()

    #permite que un médico se registre en la clínica proporcionando su nombre, cédula profesional, especialidades 
    #y cédulas de especialidad.
    def registrarse_medico(self):
        # Solicita al médico ingresar su nombre, cédula profesional, especialidades y cédulas de especialidad.
        nombre = input("Ingrese su nombre: ")
        cedula_profesional = input("Ingrese su cédula profesional: ")
        especialidades = input("Ingrese sus especialidades (separadas por comas): ").split(',')
        cedulas_especialidad = input("Ingrese las cédulas de especialidad (separadas por comas): ").split(',')

        # Creamos una instancia de la clase "Medico" con los datos ingresados.
        medico = Medico(nombre, cedula_profesional, especialidades, cedulas_especialidad)

        # Agregamos al médico a la lista de médicos en la clínica.
        self.__medicos.append(medico)

        # Mostramos un mensaje de bienvenida al médico.
        print(f"Bienvenido, Dr. {nombre}!")

        # Guarda la lista actualizada de médicos en un archivo.
        self.guardar_medicos_en_archivo()

    #guardamos la lista de médicos registrados en un archivo llamado "medicos.dat"
    def guardar_medicos_en_archivo(self):
        try:
            # Intentamos abrir el archivo "medicos.dat" en modo escritura binaria ("wb").
            with open("medicos.dat", "wb") as archivo:
                # Utiliza pickle para guardar la lista de médicos en el archivo.
                pickle.dump(self.__medicos, archivo)
            # Mostramos un mensaje de confirmación si la operación fue exitosa.
            print("Médicos registrados guardados en el archivo 'medicos.dat'.")
        except IOError as e:
            # En caso de error, muestra un mensaje de error.
            print(f"Error al guardar médicos en el archivo: {e}")

    #Permite a un médico buscar y consultar el expediente clínico de un paciente
    def consultar_expediente_medico(self):
        while True:
            nombre_paciente = input("Ingresa nombre del paciente a buscar: ")
            paciente = None

            try:
                # Intentamos abrir y cargar el archivo del expediente clínico del paciente.
                with open(f"{nombre_paciente}_expediente.dat", "rb") as archivo:
                    # Carga el contenido del archivo y lo asigna a la variable 'expediente'.
                    expediente = pickle.load(archivo)
                    # Extraemos y asigna información específica del expediente clínico a variables separadas.
                    paciente = expediente.paciente
                    historial_medico = expediente.historial_medico
                    historial_vacunas = expediente.historial_vacunas

                    # Mostramos la información del expediente clínico.
                    print("Expediente Clínico:")
                    print(paciente)
                    print(historial_medico)
                    print(historial_vacunas)
                break
            except FileNotFoundError:
                # Si no se encuentra el expediente clínico, muestra un mensaje y pregunta si se desea intentar de nuevo.
                print(f"No se encontró un expediente clínico para {nombre_paciente}.")
                respuesta = input("¿Quieres intentar de nuevo? (s/n): ")
                if respuesta.lower() != 's':
                    break
        if paciente:
            try:
                # Intentamos abrir y leer el archivo de receta médica del paciente.
                with open(f"{paciente.get_nombre_paciente()}_receta_medica.txt", "r") as archivo:
                    contenido = archivo.read()
                    #Imprimimos lo que cargo el archivo
                    print(contenido)
            except FileNotFoundError:
                # Si no se encuentra la receta médica, muestra un mensaje correspondiente.
                print(f"No se encontró una receta médica para {paciente.get_nombre_paciente()}.")
    
    #este menú ofrece funcionalidades específicas para pacientes, como la creación de expedientes clínicos
    #y la visualización de la lista de pacientes registrados en la clínica
    def menu_paciente(self):
        while True:
            self.borrar()
            print("\n---- Menú Paciente ----")
            print("1. Nuevo usuario")
            print("2. Usuario registrado")
            print("3. Regresar")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.borrar()
                self.crear_expediente_clinico()
            elif opcion == "2":
                self.borrar()
                self.mostrar_pacientes()
            elif opcion == "3":
                self.menu_principal()
            else:
                print("Opción no válida. Intente de nuevo.")
            self.pausa()

# Este método carga los expedientes clínicos de pacientes desde el archivo presente en el directorio actual.
    def cargar_expedientes_desde_archivos(self):
        for filename in os.listdir('.'):
            if filename.endswith("_expediente.dat"):
                # Si el archivo tiene un nombre que termina en "_expediente.dat," lo abre en modo lectura binaria ("rb").
                with open(filename, 'rb') as archivo:
                    # Carga el contenido del archivo y lo asigna a la variable 'expediente'.
                    expediente = pickle.load(archivo)
                    # Agrega el expediente a la lista '__expedientes_clinico' que contiene todos los expedientes clínicos.
                    self.__expedientes_clinico.append(expediente)


    # Este método guarda la lista de expedientes clínicos en un archivo específico.
    def guardar_expedientes_en_archivo(self, nombre_archivo):
        # Abre un archivo en modo escritura binaria ("wb") con el nombre especificado.
        with open(nombre_archivo, 'wb') as archivo:
            # Utiliza la biblioteca pickle para serializar y guardar la lista '__expedientes_clinico' en el archivo.
            pickle.dump(self.__expedientes_clinico, archivo)

# Este método permite a un paciente crear su propio expediente clínico proporcionando información personal, historial médico y registros de vacunación.
    def crear_expediente_clinico(self):
        #Se recopila la información sobre paciente.
        print("\nBienvenido a la clínica. Por favor, complete su expediente clínico.")
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
        genero = input("Ingrese su género: ")
        num_seguro_social = input("Ingrese su número de seguro social: ")
        direccion = input("Ingrese su dirección: ")
        telefono = input("Ingrese su número de teléfono: ")
        correo = input("Ingrese su correo electrónico: ")
        nombre_contacto_emergencia = input("Ingrese el nombre del contacto de emergencia: ")

        # Se crea un objeto 'Paciente' con la información personal proporcionada por el paciente.
        paciente = Paciente(nombre, edad, fecha_nacimiento, genero, num_seguro_social, direccion, telefono, correo, nombre_contacto_emergencia)
        
        print(f"Bienvenido, {nombre}! Ha sido registrado en la clínica.")

        # Se recopila información adicional sobre el historial médico del paciente.
        alergias = input("Alergias: ")
        enfermedades_cronicas = input("Enfermedades crónicas: ")
        procedimientos_quirurgicos = input("Procedimientos quirúrgicos previos: ")
        enfermedades_hereditarias = input("Enfermedades hereditarias: ")
        condiciones_familiares = input("Condiciones médicas en la familia: ")
        peso = input("Peso: ")
        talla = input("Talla: ")

        # Se crea un objeto 'HistorialMedico' con la información recopilada.
        historial_medico = HistorialMedico(alergias, enfermedades_cronicas, procedimientos_quirurgicos, enfermedades_hereditarias, condiciones_familiares, peso, talla)

        # Se crea un objeto 'HistorialVacunas' para registrar las vacunas.
        historial_vacunas = HistorialVacunas()

        # Se permite al paciente ingresar información sobre las vacunas que ha recibido con un bucle.
        while True:
            nombre_vacuna = input("Ingrese el nombre de la vacuna (o 'fin' para salir): ")
            if nombre_vacuna.lower() == 'fin':
                break

            fecha_vacuna = input("Ingrese la fecha de la vacuna (YYYY-MM-DD): ")
            # Se agrega la vacuna al historial de vacunas.
            historial_vacunas.agregar_vacuna(nombre_vacuna, fecha_vacuna)

        # Se crea un objeto 'ExpedienteClinico' que combina toda la información recopilada.
        expediente = ExpedienteClinico(paciente, historial_medico, historial_vacunas)

        # El expediente se agrega a la lista de expedientes clínicos de la clínica.
        self.__expedientes_clinico.append(expediente)

        # Se guarda el expediente en un archivo con el nombre del paciente.
        with open(f"{paciente.get_nombre_paciente()}_expediente.dat", "wb") as archivo:
            pickle.dump(expediente, archivo)

        print("Expediente clínico creado con éxito.")


    # Este método permite a un paciente buscar su expediente clínico proporcionando su nombre.
    def mostrar_pacientes(self):
        nombre_paciente = input("Ingrese su nombre para buscar su expediente: ")

        # Inicialmente, no se ha encontrado ningún paciente.
        paciente_encontrado = None

        # Se recorre la lista de expedientes clínicos en busca del paciente por su nombre.
        for expediente in self.__expedientes_clinico:
            if expediente.paciente.get_nombre_paciente().lower() == nombre_paciente.lower():
                paciente_encontrado = expediente.paciente
                break

        # Se muestra una lista de todos los pacientes registrados en la 
        #clínica con ayuda de los metodos de pacinete.
        print("\nLista de pacientes registrados:")
        for expediente in self.__expedientes_clinico:
            paciente = expediente.paciente
            print(f"Nombre: {paciente.get_nombre_paciente()}")
            print(f"Edad: {paciente.get_edad_paciente()}")
            print(f"Género: {paciente.get_genero()}")
            print("-" * 40)

        # Si el paciente no se encuentra en la lista de expedientes, se muestra un mensaje para registrarse primero.
        if not paciente_encontrado:
            print("\nNo se encuentra un expediente para el paciente. Por favor, regístrese primero.")
            return

        # Si se encuentra el paciente, se muestra un menú para que el paciente realice acciones relacionadas con su expediente.
        print(f"\n----Bienvenido {paciente_encontrado.get_nombre_paciente()}---")

        #Menú interactivo para pacientes que les permite realizar varias acciones relacionadas con su expediente médico. 
        while True:
            self.borrar()
            print(f"\n---- Menú Paciente {paciente_encontrado.get_nombre_paciente()} ----")
            print("1. Solicitar Consulta")
            print("2. Consultar Expediente")
            print("3. Regresar")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.borrar()
                self.solicitar_consulta(paciente_encontrado)
            elif opcion == "2":
                self.borrar()
                self.consultar_expediente_paciente(paciente_encontrado)
            elif opcion == "3":
                self.menu_paciente()
            else:
                print("Opción no válida. Intente de nuevo.")
            self.pausa()


    # Este método permite a un paciente consultar su expediente médico.
    def consultar_expediente_paciente(self, paciente_encontrado):
        expediente_encontrado = None

        # Busca el expediente clínico del paciente entre los expedientes de la clínica.
        for expediente in self.__expedientes_clinico:
            if expediente.paciente == paciente_encontrado:
                expediente_encontrado = expediente
                break

        # Si se encuentra el expediente, se obtiene información relevante como el paciente, el historial médico y el historial de vacunas.
        paciente = expediente_encontrado.paciente
        historial_medico = expediente_encontrado.historial_medico
        historial_vacunas = expediente_encontrado.historial_vacunas

        if expediente_encontrado:
            # Muestra en pantalla la información del expediente, incluyendo los datos del paciente, su historial médico y su historial de vacunas.
            print("\nExpediente encontrado:")
            print(paciente)
            print(historial_medico)
            print(historial_vacunas)

            # Intentamos abrir y leer un archivo de receta médica específico para el paciente.
            nombre_archivo_receta = f"{paciente.get_nombre_paciente()}_receta_medica.txt"
            try:
                with open(nombre_archivo_receta, 'r') as archivo_receta:
                    contenido_receta = archivo_receta.read()
                    print(contenido_receta)
            except FileNotFoundError:
                # Si el archivo de receta no se encuentra, muestra un mensaje indicando que no se encontró una receta para el paciente.
                print(f"No se encontró un archivo de receta para {paciente.get_nombre_paciente()}.")

            
    # El paciente solicita una consulta médica.
    def solicitar_consulta(self, paciente):
        print("\n--- Solicitud de Consulta ---")

        # El paciente ingresa sus síntomas, separados por coma.
        sintomas = input("Ingrese sus síntomas (separados por coma): ").split(',')

        # Se obtiene la fecha actual sin la hora.
        fecha_actual = datetime.datetime.now()
        fecha_sin_hora = fecha_actual.date()

        # Se crea una receta médica con los datos del paciente, la fecha, los síntomas y el nombre del hospital.
        receta = Receta(paciente, fecha_sin_hora, None, sintomas, None, None, "Hospital ABC")
        
        # Se imprime y se guarda la receta médica.
        receta.imprimir_receta_y_guardar()

        # Luego, se consulta el expediente del paciente para mostrar la información actualizada.
        self.consultar_expediente_paciente(paciente)

# Se crea una instancia de la clase Clinica.
clinica = Clinica()

# Se inicia el menú principal de la clínica.
clinica.menu_principal()



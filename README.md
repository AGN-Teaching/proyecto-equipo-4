## Introducción
En este informe se muetra la implementación de sistemas de gestión médica que  es esencial para mejorar la eficiencia y calidad en la atención a los pacientes. Este proyecto se aborda la necesidad de la clínica médica de incorporar un Expediente Clínico Electrónico, brindando una solución integral para el seguimiento y registro de la atención médica.

## Análisis del Problema:
La adopción de un Expediente Clínico Electrónico responde a la demanda específica de una clínica médica que busca optimizar sus operaciones. En este contexto, se identifican aspectos clave, como la diversidad de especialidades médicas ofrecidas y la necesidad de gestionar eficientemente la información asociada a cada paciente. En el código presenta una implementación de programación orientada a objetos (POO), destacando por su organización en clases que representan entidades específicas como pacientes, médicos y medicamentos.  Además, se observan principios clave de POO como el encapsulamiento, la abstracción y la persistencia de datos mediante la serialización con pickle , respaldada por un manejo adecuado de excepciones. En conjunto, estas características demuestran la aplicación exitosa de los principios de POO, proporcionando una estructura modular, mantenible y escalable para el sistema de gestión clínica.



##Elección de Clases

####  Paciente

**Funcionamiento: **Representa a los individuos que reciben atención médica. Contiene información personal y sirve como punto central para la asociación de datos médicos.
**Justificación: **La clase Paciente es fundamental, ya que establece la identidad única de cada individuo y sirve como ancla para la información médica relacionada.

------------

#### Médico
*Funcionamiento:* Representa a los profesionales de la salud que atienden a los pacientes. Asocia médicos con  especialidades.
*Justificación:* Facilita la gestión de los recursos médicos al asignar eficientemente pacientes según especialidades.

------------
#### Medicamento

*Funcionamiento:* Almacena información sobre los medicamentos utilizados en tratamientos. Asociado a recetas.
*Justificación:* Necesario para detallar tratamientos recetados, proporcionando información esencial sobre medicamentos y dosis.

------------
#### Especialidad

*Funcionamiento:* Organiza y categoriza las diferentes áreas médicas de especialización.
*Justificación:* Permite la clasificación de médicos según sus habilidades y facilita la asignación de pacientes a profesionales con conocimientos específicos.

------------

#### Expediente Clínico
**Funcionamiento: **Relaciona y organiza la información médica de un paciente, sus consultas y recetas asociadas.
*Justificación:* Actúa como núcleo central del sistema, proporcionando una estructura que integra y relaciona todos los aspectos médicos de un paciente.

------------

#### Historial Médico
**Funcionamiento: **Almacena el historial médico de un paciente, incluyendo alergias y enfermedades crónicas.
*Justificación:* Ofrece una visión completa de la salud del paciente, facilitando diagnósticos y tratamientos precisos.

------------

#### Historial Vacunas

*Funcionamiento:* Almacena el historial de vacunas de un paciente.
*Justificación: *  Contribuye a la gestión preventiva de la salud, registrando fechas y tipos de vacunas aplicadas.


------------

#### Receta Médica
*Funcionamiento:* Asocia medicamentos y dosis a un paciente y una consulta médica específica.
**Justificación: **Permite la prescripción y seguimiento de tratamientos médicos, conectando médicos, pacientes y medicamentos.

------------

#### Historial Vacunas

**Funcionamiento: **Almacena el historial de vacunas de un paciente.
*Justificación:* Contribuye a la gestión preventiva de la salud, registrando fechas y tipos de vacunas aplicadas.

------------

#### Estudio Médico

*Funcionamiento:* Representa análisis y estudios médicos específicos realizados a un paciente.
*Justificación:* Permite el registro  de procedimientos médicos, contribuyendo a evaluaciones y diagnósticos precisos.

------------

#### Cirugía
*Funcionamiento:* Registra información relacionada con intervenciones quirúrgicas realizadas a un paciente.
*Justificación:* Permite el seguimiento de procedimientos quirúrgicos, integrando información vital en el expediente clínico.

------------


#### Clinica
*Funcionamiento:* Representa la entidad principal que engloba todas las operaciones y gestión de recursos médicos. Controla la interacción entre pacientes, médicos y datos médicos.
*Justificación:* La clase Clinica actúa como el punto central del sistema, coordinando las operaciones de consulta, registro de pacientes, asignación de médicos y almacenamiento de datos médicos.

------------


## 2. Diagrama UML

------------
#### Clase Paciente

##### Atributos:

-nombre: str
-edad: int
-fecha_nacimiento: str
-genero: str
-num_seguro_social: str
-direccion: str
-telefono: str
-correo_electronico: str
-contacto_emergencia: str
##### Métodos:

+get_edad_paciente(): int
+get_nombre_paciente(): str
+get_genero(): str


#### Clase Receta

##### Atributos:

-paciente: Paciente
-fecha: str
-historial_medico: HistorialMedico
-sintomas: List[str]
-instrucciones: str
-duracion: str
-nombre_clinica: str
##### Métodos:

+obtener_informacion_expediente(): Tuple[Optional[HistorialMedico], Optional[Paciente]] (Obtiene información del expediente médico del paciente)
+buscar_y_mostrar_medicamentos(sintomas: List[str]): List[Tuple[str, List[str], str]] (Busca y muestra medicamentos según los síntomas proporcionados)
+imprimir_receta_y_guardar(): void (Imprime y guarda la receta médica)

#### Clase Especialidad

##### Atributos:

-especialidades: List[Tuple[str, str]] (Lista de tuplas que contiene el nombre y descripción de cada especialidad médica)
##### Métodos:

+agregar_especialidad(nombre: str, descripcion: str): void (Agrega una nueva especialidad a la lista)
+mostrar_especialidades(): void (Muestra la lista de especialidades con sus nombres y descripciones)
+borrar_especialidad(nombre: str): void (Elimina una especialidad de la lista por su nombre)
+get_especialidad(nombre: str): Optional[Tuple[str, str]] (Devuelve la información de una especialidad por su nombre)
+mostrar_especialidades_nombre(): void (Muestra solo los nombres de las especialidades)

#### Clase Cirugia

##### Atributos:

-nombre_cirugia: str
-cirugias: List[Tuple[str, str]] (Lista de tuplas que contiene el nombre y los síntomas de cada cirugía)

##### Métodos:

+cargar_cirugias_desde_archivo(nombre_archivo: str): void (Carga la lista de cirugías desde un archivo binario)
+buscar_cirugia(sintomas_paciente: List[str]): Union[str, List[Tuple[str, str]]] (Busca cirugías según los síntomas proporcionados)

#### Clase EstudioMedico

Atributos:
-tipo_estudio: str

##### Métodos:

+cargar_estudios_desde_archivo(nombre_archivo: str): void (Carga la lista de estudios médicos desde un archivo binario)
+buscar_estudio_medico(sintomas_paciente: List[str]): Union[str, List[Tuple[str, str]]] (Busca estudios médicos según los síntomas proporcionados)
+buscar_y_mostrar_estudio_medico(sintoma: str): List[Tuple[str, str]] (Busca y muestra estudios médicos según el síntoma proporcionado)

#### Clase ExpedienteClinico

##### Atributos:

+paciente: Paciente
+historial_vacunas: HistorialVacunas
+historial_medico: HistorialMedico

#### Clase HistorialMedico

##### Atributos:

-alergias: str
-enfermedades_cronicas: str
-procedimientos_quirurgicos: str
-enfermedades_hereditarias: str
-condiciones_familiares: str
-peso: float
-talla: float

##### Métodos:

+get_alergias(): str
+get_peso(): float
+get_talla(): float

#### Clase HistorialVacunas

##### Atributos:

+vacunas: List[Dict[str, str]] (Lista de diccionarios que contiene el nombre y fecha de cada vacuna)


##### Métodos:

+agregar_vacuna(nombre: str, fecha: str): void (Agrega una nueva vacuna a la lista)
+str(): str (Devuelve una representación en cadena del historial de vacunas)

#### Clase Medicamento

##### Atributos:

-medicamentos: List[Tuple[str, str, str]] (Lista de tuplas que contiene el nombre, síntomas, y dosis de cada medicamento)

##### Métodos:

+agregar_medicamento(nombre: str, sintomas: List[str], dosis: str, nombre_archivo: str): void (Agrega un nuevo medicamento a la lista)
+cargar_medicamentos_desde_archivo(nombre_archivo: str): void (Carga la lista de medicamentos desde un archivo binario)
+buscar_y_mostrar_medicamentos(sintoma: str): List[Tuple[str, List[str], str]] (Busca y muestra medicamentos según el síntoma proporcionado)
+eliminar_medicamento(nombre: str): void (Elimina un medicamento de la lista por su nombre)
+mostrar_medicamentos(): void (Muestra la lista de medicamentos con sus nombres, síntomas y dosis)
+mostrar_medicamento_nombre(): void (Muestra solo los nombres de los medicamentos)

#### Clase Medico

##### Atributos:

-nombre_medico: str
-cedula_profesional: str
-especialidades: List[str]
-cedulas_especialidad: List[str]

##### Métodos:

+get_nombre_medico(): str
+get_cedula_profesional(): str
+eliminar_medico(cedula: str): void (Elimina un médico de la lista por su cédula)
+mostrar_medicos(): void (Muestra la lista de médicos con sus nombres, cédulas y especialidades)
+mostrar_nombres_cedulas(): void (Muestra solo los nombres y cédulas de los médicos)

#### Clase Clinica

##### Atributos :

-expedientes_clinico: Lista de expedientes clínicos cargados.
-medicos: Lista de médicos registrados en la clínica.
-medicamento: Lista de medicamentos cargados.
-especialidad: Lista de especialidades médicas cargadas.
-especialidades: Instancia de la clase Especialidad.
-lista_medicos: Instancia de la clase Medico para gestionar la lista de médicos.
-medicamentos: Instancia de la clase Medicamento para gestionar la lista de medicamentos.

##### Métodos:


+cargar_medicamentos(): Carga la lista de medicamentos desde el archivo "medicamentos.dat".
+cargar_especialidades(): Carga la lista de especialidades médicas desde el archivo "especialidades_medicas.dat".
+cargar_expedientes(): Carga la lista de expedientes clínicos desde los archivos *_expediente.dat en el directorio.
+cargar_medicos(): Carga la lista de médicos desde el archivo "medicos.dat".
+menu_principal(): Método principal para el menú principal de la aplicación.
+menu_administrador(): Menú para las opciones de administrador.
+eliminar_paciente(nombre): Elimina un paciente y su expediente clínico.
+eliminar_medico(): Elimina un médico de la lista de médicos.
+eliminar_medicamento(): Elimina un medicamento de la lista de medicamentos.
+eliminar_especialidad(): Elimina una especialidad de la lista de especialidades médicas.
+agregar_especialidades(): Agrega una nueva especialidad a la lista.
+agregar_medicamento(): Agrega un nuevo medicamento a la lista.
+mostrar_medicamentos(): Muestra la lista de medicamentos.
+mostrar_medicos(): Muestra la lista de médicos.
+mostrar_especialidades(): Muestra la lista de especialidades médicas.
+consultar_expediente_administrador(): Consulta y muestra un expediente clínico desde el punto de vista del administrador.
+eliminar_paciente(nombre): Elimina el expediente clínico de un paciente según el nombre.
+eliminar_medico(): Elimina un médico de la lista y su archivo asociado.
+eliminar_medicamento(): Elimina un medicamento de la lista y su archivo asociado.
+eliminar_especialidad(): Elimina una especialidad de la lista y su archivo asociado.
+agregar_especialidades(): Agrega una nueva especialidad a la lista y guarda la información en el archivo.
+agregar_medicamento(): Agrega un nuevo medicamento a la lista y guarda la información en el archivo.
+mostrar_medicamentos(): Muestra la lista de medicamentos.
+mostrar_medicos(): Muestra la lista de médicos.
+mostrar_especialidades(): Muestra la lista de especialidades médicas.
+guardar_medicos_en_archivo(): Guarda la lista de médicos en el archivo "medicos.dat".
consultar_expediente_medico(): Consulta y muestra un expediente clínico desde el punto de vista del médico.
+menu_medico(): Menú para las opciones del médico.
+registrarse_medico(): Registra a un nuevo médico.
+guardar_medicos_en_archivo(): Guarda la lista de médicos en el archivo "medicos.dat".
+consultar_expediente_medico(): Consulta y muestra un expediente clínico desde el punto de vista del médico.
+menu_paciente(): Menú para las opciones del paciente.
+cargar_expedientes_desde_archivos(): Carga los expedientes clínicos desde los archivos *_expediente.dat.
+guardar_expedientes_en_archivo(nombre_archivo): Guarda los expedientes clínicos en un archivo específico.
+crear_expediente_clinico(): Crea un nuevo expediente clínico para un paciente.
+mostrar_pacientes(): Muestra la lista de pacientes registrados.
+consultar_expediente_paciente(paciente_encontrado): Consulta y muestra un expediente clínico desde el punto de vista del paciente.
+solicitar_consulta(paciente): Permite al paciente solicitar una consulta y genera una
 receta médica.
 
### Diagrama UML


### Concluciones

##### Samuel Pérez Pérez: 
En el desarrollo de este proyecto de Expediente Clínico Electrónico, he aplicado los principios fundamentales de la programación orientada a objetos (POO). La implementación de clases especializadas para representar entidades a través de la abstracción, he generado un diseño modular eficiente y la reutilización efectiva de código, junto con la persistencia de datos. Este proyecto ha fortalecido mi habilidad para enfrentar problemas y resolverlos mediante la aplicación de conceptos de programación.

##### Saul Rovelo Lopez:
El programa es una aplicación básica de gestión de expedientes clinicos. Se centra en la interacción a través de menús y opciones de usuario, proporcionando una estructura modular que permite a los diferentes usuarios realizar tareas específicas de acuerdo a su rol. Además de su funcionalidad básica, el programa también demuestra buenas prácticas de programación, como la organización en clases y métodos, lo que facilita la comprensión y el mantenimiento del código. También utiliza manejo de excepciones para gestionar errores y situaciones inesperadas de manera más robusta.

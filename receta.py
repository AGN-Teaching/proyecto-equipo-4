from medicamentos import Medicamento
import pickle
from cirugia import Cirugia
from estudio_medico import EstudioMedico
class Receta:
    def __init__(self, paciente, fecha, historial_medico, sintomas, instrucciones, duracion, nombre_clinica="Hospital ABC"):

        self.paciente = paciente
        self.historial_medico = historial_medico
        self.nombre_clinica = nombre_clinica
        self.fecha = fecha
        self.sintomas = sintomas
        self.duracion = duracion
        self.instrucciones = instrucciones

    # Método para obtener información del expediente médico del paciente.
    def obtener_informacion_expediente(self):

        try:
            # Carga el expediente médico del paciente desde un archivo binario.
            with open(f"{self.paciente.get_nombre_paciente()}_expediente.dat", "rb") as archivo:
                expediente = pickle.load(archivo)

                # Comprueba si hay historial médico en el expediente y lo devuelve junto con los datos del paciente.
                if expediente.historial_medico:
                    return expediente.historial_medico, expediente.paciente
                else:
                    print("No se encontró información médica en el expediente.")
                    return None, None
                #Si no encuentra un archivo crea una excepcion que nos muestra los mensajes
        except FileNotFoundError:
            print(f"No se encontró un expediente clínico para {self.paciente.get_nombre_paciente()}.")
            return None, None
        except Exception as e:
            print(f"Error al cargar el expediente: {e}")
            return None, None

    # Método para buscar y mostrar medicamentos relacionados con los síntomas.
    def buscar_y_mostrar_medicamentos(self, sintomas):
        
        # Crea una instancia de la clase Medicamento.
        mi_medicamento = Medicamento()

        # Utiliza el objeto mi_medicamento para buscar medicamentos relacionados con los síntomas proporcionados.
        medicamentos_encontrados = mi_medicamento.buscar_y_mostrar_medicamentos(sintomas)

        # Devuelve los medicamentos encontrados.
        return medicamentos_encontrados

    # Método para imprimir y guardar la receta médica.
    def imprimir_receta_y_guardar(self):

        # Obtiene información del expediente médico del paciente.
        historial_medico, paciente = self.obtener_informacion_expediente()

        if paciente and historial_medico:
            # Variable con el nombre del archivo para guardar la receta.
            nombre_archivo = f"{paciente.get_nombre_paciente()}_receta_medica.txt"
            try:
                with open(nombre_archivo, 'w') as archivo:
                    # Escribe la información de la receta en el archivo.
                    archivo.write("\n\nRECETA MEDICA\n")
                    archivo.write(f"\nClínica: {self.nombre_clinica}    Fecha: {self.fecha}\n")
                    archivo.write("\nMedico general: Rafael Lopez Gatel\n")
                    archivo.write(f"\nPaciente: {paciente.get_nombre_paciente()}     Edad: {paciente.get_edad_paciente()}\n")
                    archivo.write(f"Peso: {historial_medico.get_peso() }\n")
                    archivo.write(f"Talla: {historial_medico.get_talla()}\n")
                    archivo.write(f"Alergias: {historial_medico.get_alergias()}\n")
                    archivo.write("-----------------------------------------------\n")

                    # Busca y muestra medicamentos relacionados con los síntomas.
                    medicamentos_encontrados = self.buscar_y_mostrar_medicamentos(self.sintomas)
                    if isinstance(medicamentos_encontrados, list):
                        archivo.write("\nMedicamentos recetados:\n")
                        for medicamento in medicamentos_encontrados:
                            archivo.write(f"Nombre: {medicamento[0]}\n")
                            archivo.write(f"Síntomas: {medicamento[1]}\n")
                            archivo.write(f"Dosis: {medicamento[2]}\n")
                            archivo.write("-" * 30 + "\n")

                    # Carga cirugias desde un archivo y busca cirugias relacionadas con los síntomas.
                    mi_cirugia = Cirugia()
                    mi_cirugia.cargar_cirugias_desde_archivo("cirujias.dat")
                    cirugias_encontradas = mi_cirugia.buscar_cirugia(self.sintomas)
                    if isinstance(cirugias_encontradas, list):
                        archivo.write("Cirugías encontradas para los síntomas proporcionados por el paciente:\n")
                        for cirugia in cirugias_encontradas:
                            archivo.write(f"Nombre: {cirugia[0]}\n")
                            archivo.write(f"Síntomas: {cirugia[1]}\n")
                            archivo.write("-" * 30 + "\n")

                    # Carga estudios médicos desde un archivo y busca estudios médicos relacionados con los síntomas.
                    mi_estudio_medico = EstudioMedico()
                    mi_estudio_medico.cargar_estudios_desde_archivo("estudios_medicos.dat")
                    estudios_encontrados = mi_estudio_medico.buscar_estudio_medico(self.sintomas)
                    if isinstance(estudios_encontrados, list):
                        archivo.write("Estudios médicos encontrados para los síntomas proporcionados por el paciente:\n")
                        for estudio_medico in estudios_encontrados:
                            archivo.write(f"Nombre: {estudio_medico[0]}\n")
                            archivo.write(f"Síntomas: {estudio_medico[1]}\n")
                            archivo.write("-" * 30 + "\n")

                print(f"La receta médica se ha guardado correctamente en {nombre_archivo}")
            except Exception as e:
                print(f"Error al guardar la receta médica: {e}")
        else:
            print("No se puede imprimir la receta. Paciente no encontrado o información médica no disponible.")

class HistorialVacunas:
    def __init__(self):

        self.vacunas = []

    # Método para agregar una nueva vacuna al historial.
    def agregar_vacuna(self, nombre, fecha):

        # Crea un diccionario con el nombre y la fecha de la vacuna y lo agrega a la lista de vacunas.
        vacuna = {"Nombre": nombre, "Fecha": fecha}
        self.vacunas.append(vacuna)

    # Método para obtener una representación en cadena del objeto HistorialVacunas.
    def __str__(self):
        
        # Devuelve una cadena que muestra cada vacuna registrada en el historial, incluyendo su nombre y fecha.
        return "\n".join(f"Vacuna: {v['Nombre']} - Fecha: {v['Fecha']}" for v in self.vacunas)

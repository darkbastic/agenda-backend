class Estudio:
    def __init__(self, id, fecha, asignatura, contenido, completado):
        self.id = id
        self.fecha = fecha
        self.asignatura = asignatura
        self.contenido = contenido
        self.completado = completado

    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "asignatura": self.asignatura,
            "contenido": self.contenido,
            "completado": self.completado
        }
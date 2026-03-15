class Control:

    def __init__(self, id, fecha, asignatura, contenido, descripcion):
        self.id = id
        self.fecha = fecha
        self.asignatura = asignatura
        self.contenido = contenido
        self.descripcion = descripcion


    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha.isoformat() if self.fecha else None,
            "asignatura": self.asignatura,
            "contenido": self.contenido,
            "descripcion": self.descripcion
        }
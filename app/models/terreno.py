class Terreno:

    def __init__(self, id, fecha, asignatura, lugar, direccion):
        self.id = id
        self.fecha = fecha
        self.asignatura = asignatura
        self.lugar = lugar
        self.direccion = direccion


    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "asignatura": self.asignatura,
            "lugar": self.lugar,
            "direccion": self.direccion
        }
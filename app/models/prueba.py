class Prueba:
   
   def __init__(self, fecha, contenido, asignatura, ponderacion, descripcion=None):
        self.fecha = fecha
        self.contenido = contenido
        self.asignatura = asignatura
        self.ponderacion = ponderacion
        self.descripcion = descripcion
    
   def to_dict(self):
        return {
            "fecha": self.fecha,
            "contenido": self.contenido,
            "asignatura": self.asignatura,
            "ponderacion": self.ponderacion,
            "descripcion": self.descripcion
        }
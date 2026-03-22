from app.database.connection import get_connection

class EstudioController:
    
    def crear_estudio(self, data):

        if not data.get("fecha"):
            return {"error": "La fecha es obligatoria"}
        
        if not data.get("asignatura"):
            return {"error": "La asignatura es obligatoria"}

        conn = get_connection()
        cursor = conn.cursor() 
        cursor.execute("""
            INSERT INTO estudio (fecha, asignatura, contenido)
            VALUES (%s,%s,%s)
            RETURNING id
        """,
        (data['fecha'],
         data['asignatura'],
         data['contenido']
        ))

        new_id = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return {
            "id": new_id,
            "fecha": data["fecha"],
            "asignatura": data["asignatura"],
            "contenido": data["contenido"]
        }, 201
    
    def get_estudios(self):

        conn = get_connection()
        cursor = conn.cursor()         

        cursor.execute("""
            SELECT id, fecha, asignatura, contenido, completado
            FROM estudio
            ORDER BY fecha asc
        """)

        rows = cursor.fetchall()
        estudios = []

        for row in rows:
            estudio = {
                "id": row[0],
                "fecha": row[1],
                "asignatura": row[2],
                "contenido": row[3],
                "completado": row[4]
            } 
            estudios.append(estudio)
        
        cursor.close()
        conn.close()

        return estudios
    
    def get_estudios_semana(self, fecha_inicio):

        if not fecha_inicio:
            return {"error": "La fecha de inicio es obligatoria"}
        
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, fecha, asignatura, contenido, completado
            FROM estudio
            WHERE fecha BETWEEN %s AND %s::date + INTERVAL '6 days'
            ORDER BY fecha ASC     
        """,(fecha_inicio,fecha_inicio))

        rows = cursor.fetchall()
        estudios = []

        for row in rows:
            estudio = {
                "id": row[0],
                "fecha": row[1],
                "asignatura": row[2],
                "contenido": row[3],
                "completado": row[4]
            } 
            estudios.append(estudio)

        cursor.close()
        conn.close()

        return estudios
    
    def update_estudio(self, id, data):
    
        if not data.get("fecha"):
            return {"error": "La fecha es obligatoria"}
    
        if not data.get("asignatura"):
            return {"error": "La asignatura es obligatoria"}
    
        conn = get_connection()
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE estudio
            SET fecha = %s,
                asignatura = %s,
                contenido = %s
            WHERE id = %s
            RETURNING id
        """, (
            data["fecha"],
            data["asignatura"],
            data.get("contenido"),
            id
        ))
    
        updated = cursor.fetchone()
    
        if not updated:
            cursor.close()
            conn.close()
            return {"error": "Estudio no encontrado"}
    
        conn.commit()
        cursor.close()
        conn.close()
    
        return {
            "id": id,
            "fecha": data["fecha"],
            "asignatura": data["asignatura"],
            "contenido": data.get("contenido")
        }
    
    def eliminar_estudio(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM estudio
            WHERE id = %s
            RETURNING id 
        """,(id,))

        deleted = cursor.fetchone()
        if not deleted:
            cursor.close()
            conn.close()
            return {"error": "Estudio no encontrada"}

        conn.commit()
        cursor.close()
        conn.close()
        
        return {
            "id": deleted[0]
        }          
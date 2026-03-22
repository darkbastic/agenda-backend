from app.database.connection import get_connection

class PruebasController:
    
    def get_pruebas(self):

        conn = get_connection()
        cursor = conn.cursor()

        sql = """        
        SELECT id, fecha, asignatura, contenido, ponderacion, descripcion
        FROM pruebas
        ORDER BY fecha ASC
        """
        cursor.execute(sql)

        rows = cursor.fetchall()

        pruebas = []

        for row in rows:
            prueba = {
                "id": row[0],
                "fecha": row[1],
                "asignatura": row[2],
                "contenido": row[3],
                "ponderacion": row[4],
                "descripcion": row[5]
            }
            pruebas.append(prueba)

        cursor.close()
        conn.close()

        return pruebas
    

    def create_prueba(self, data):

        if not data.get("fecha"):
            return {"error": "La fecha es obligatoria"}
    
        if not data.get("asignatura"):
            return {"error": "La asignatura es obligatoria"}
    
        if not data.get("contenido"):
            return {"error": "El contenido es obligatorio"}
    
        if not data.get("ponderacion"):
             return {"error": "La ponderación es obligatoria"}

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pruebas (fecha, asignatura, contenido, ponderacion, descripcion)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (
            data["fecha"],
            data["asignatura"],
            data["contenido"],
            data["ponderacion"],
            data.get("descripcion")
        ))
        new_id = cursor.fetchone()[0]

        conn.commit()
        cursor.close()
        conn.close()

        return {
            "id": new_id,
            "fecha": data["fecha"],
            "asignatura": data["asignatura"],
            "contenido": data["contenido"],
            "ponderacion": data["ponderacion"],
            "descripcion": data.get("descripcion")
        }, 201
    
    def update_prueba(self, id, data):
        if not data.get("fecha"):
            return {"error": "La fecha es obligatoria"}

        if not data.get("asignatura"):
            return {"error": "La asignatura es obligatoria"}

        if not data.get("contenido"):
            return {"error": "El contenido es obligatorio"}

        if not data.get("ponderacion"):
            return {"error": "La ponderación es obligatoria"}    

        conn = get_connection() 
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE pruebas
            SET fecha = %s,
                asignatura = %s,
                contenido = %s,
                ponderacion = %s,
                descripcion = %s
            WHERE id = %s
            RETURNING id, fecha, asignatura, contenido, ponderacion, descripcion
        """, (
            data["fecha"],
            data["asignatura"],
            data["contenido"],
            data["ponderacion"],
            data.get("descripcion"),
            id
        ))

        updated = cursor.fetchone()
        if not updated:
            cursor.close()
            conn.close()
            return {"error": "Prueba no encontrada"}
        
        conn.commit()
        cursor.close()  
        conn.close()

        return {
            "id": updated[0],
            "fecha": updated[1],
            "asignatura": updated[2],
            "contenido": updated[3],
            "ponderacion": updated[4],
            "descripcion": updated[5]
        }                       
    
    def delete_prueba(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM pruebas
            WHERE id = %s
            RETURNING id     
        """, (id,))

        deleted = cursor.fetchone()
        if not deleted:
            cursor.close()
            conn.close()
            return {"error": "Prueba no encontrada"}     

        conn.commit()
        cursor.close()
        conn.close()
        
        return {
            "id": deleted[0]
        }  
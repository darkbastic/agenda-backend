from app.database.connection import get_connection
from app.models.control import Control

class ControlesController:

    def get_controles(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, fecha, asignatura, contenido, descripcion
        FROM controles
        ORDER BY fecha ASC 
        """)

        rows = cursor.fetchall()
        controles = []

        for row in rows:
            control = Control(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )
            controles.append(control.to_dict())

        cursor.close()
        conn.close()

        return controles
    
    def create_control(self, data):
    
        if not data.get("fecha"):
            return {"error": "La fecha es obligatoria"}
    
        if not data.get("asignatura"):
            return {"error": "La asignatura es obligatoria"}
    
        if not data.get("contenido"):
            return {"error": "El contenido es obligatorio"}
    
        conn = get_connection()
        cursor = conn.cursor()
    
        cursor.execute("""
            INSERT INTO controles (fecha, asignatura, contenido, descripcion)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (
            data["fecha"],
            data["asignatura"],
            data["contenido"],
            data["descripcion"]
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
            "descripcion": data["descripcion"]
        }, 201
    
    def delete_control(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM controles
            WHERE id = %s
            RETURNING id   
        """,(id,))

        deleted = cursor.fetchone()
        if not deleted:
            cursor.close()
            conn.close()
            return {"error": "Control no encontrado"}
        
        conn.commit()
        cursor.close()
        conn.close()

        return {
            "id": deleted[0]
        }
    
    def actualizar_control(self, id, data):
        if not data.get("fecha"):
            return {"error": "La fecha es obligatoria"}
    
        if not data.get("asignatura"):
            return {"error": "La asignatura es obligatoria"}
    
        if not data.get("contenido"):
            return {"error": "El contenido es obligatorio"}

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE controles
            SET fecha = %s,
                asignatura = %s,
                contenido = %s,
                descripcion = %s
            WHERE id = %s
            RETURNING id, fecha, asignatura, contenido, descripcion
        """, (
            data["fecha"],
            data["asignatura"],
            data["contenido"],
            data.get("descripcion"),
            id
        ))

        updated = cursor.fetchone()
        if not updated:
            cursor.close()
            conn.close()
            return {"error": "Control no encontrado"}
        
        conn.commit()
        cursor.close()  
        conn.close()

        return {
            "id": updated[0],
            "fecha": updated[1],
            "asignatura": updated[2],
            "contenido": updated[3],
            "descripcion": updated[4]
        }          
from app.database.connection import get_connection
from app.models.terreno import Terreno

class TerrenosController:

    def get_terrenos(self):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT id, fecha, asignatura, lugar, direccion
            FROM terrenos
            ORDER BY fecha ASC
        """

        cursor.execute(sql)
        rows = cursor.fetchall()

        terrenos = []

        for row in rows:
            terreno = {
                "id": row[0],
                "fecha": row[1],
                "asignatura": row[2],
                "lugar": row[3],
                "direccion": row[4]
            }
            terrenos.append(terreno)

        cursor.close()
        conn.close()
        return terrenos

    def crear_terreno(self, data):
        if not data.get("fecha"):
            return {"mensaje":"La fecha es obligatoria"}

        if not data.get("asignatura"):
            return {"mensaje":"La asignatura es obligatoria"}
        
        if not data.get("lugar"):
            return {"mensaje":"El lugar es obligatorio"}

        if not data.get("direccion"):
            return {"mensaje":"La direccion es obligatoria"}
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO terrenos (fecha, asignatura, lugar, direccion) 
            VALUES (%s,%s,%s,%s)
            RETURNING id
        """,(
            data["fecha"],
            data["asignatura"],
            data["lugar"],
            data["direccion"]
        ))

        new_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()

        return {
            "id": new_id,
            "fecha": data["fecha"],
            "asignatura": data["asignatura"],
            "lugar": data["lugar"],
            "direccion": data["direccion"]
        }, 201
    
    def delete_terreno(id):

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM terrenos
            WHERE id = %s
            RETURNING id
        """,(id,))

        deleted = cursor.fetchone()
        if not deleted:
            cursor.close()
            conn.close()
            return {"error", "Terreno no encontrado"}
        
        conn.commit()
        cursor.close()
        conn.close()
        return {
            "id": deleted[0]
        }

    def update_terreno(self, id, data):
    
        if not data.get("fecha"):
            return {"error": "La fecha es obligatoria"}
    
        if not data.get("asignatura"):
            return {"error": "La asignatura es obligatoria"}
    
        if not data.get("lugar"):
            return {"error": "El lugar es obligatorio"}
    
        if not data.get("direccion"):
            return {"error": "La dirección es obligatoria"}
    
        conn = get_connection()
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE terrenos
            SET fecha = %s,
                asignatura = %s,
                lugar = %s,
                direccion = %s
            WHERE id = %s
            RETURNING id
        """, (
            data["fecha"],
            data["asignatura"],
            data["lugar"],
            data["direccion"],
            id
        ))
    
        updated = cursor.fetchone()
    
        if not updated:
            cursor.close()
            conn.close()
            return {"error": "Terreno no encontrado"}
    
        conn.commit()
    
        cursor.close()
        conn.close()
    
        return {
            "id": id,
            "fecha": data["fecha"],
            "asignatura": data["asignatura"],
            "lugar": data["lugar"],
            "direccion": data["direccion"]
        }
from app.database.connection import get_connection

class EventosController:

    def get_eventos(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
            'prueba' as tipo,
            id,
            fecha,
            asignatura,
            contenido,
            ponderacion,
            descripcion,
            NULL as lugar,
            NULL as direccion
            FROM pruebas
            
            UNION ALL
            
            SELECT 
            'terreno' as tipo,
            id,
            fecha,
            asignatura,
            NULL,
            NULL,
            NULL,
            lugar,
            direccion
            FROM terrenos
            
            UNION ALL
            
            SELECT 
            'control' as tipo,
            id,
            fecha,
            asignatura,
            contenido,
            NULL,
            descripcion,
            NULL,
            NULL
            FROM controles
            
            ORDER BY fecha ASC
        """)

        rows = cursor.fetchall()

        eventos = []

        for row in rows:

            evento = {
                "tipo": row[0],
                "id": row[1],
                "fecha": row[2],
                "asignatura": row[3],
                "contenido": row[4],
                "ponderacion": row[5],
                "descripcion": row[6],
                "lugar": row[7],
                "direccion": row[8]
            }

            eventos.append(evento)

        cursor.close()
        conn.close()

        return eventos
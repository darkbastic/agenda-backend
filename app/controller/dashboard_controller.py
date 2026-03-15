from app.database.connection import get_connection

class DashboardController:

    def get_dashboard(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT
        (SELECT COUNT(*) FROM pruebas) as pruebas_total,
        (SELECT COUNT(*) FROM controles) as controles_total,
        (SELECT COUNT(*) FROM terrenos) as terrenos_total,

        (SELECT COUNT(*) FROM pruebas 
         WHERE fecha BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days') as pruebas_proximos_7_dias,

        (SELECT COUNT(*) FROM controles 
         WHERE fecha BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days') as controles_proximos_7_dias,

        (SELECT COUNT(*) FROM terrenos 
         WHERE fecha BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days') as terrenos_proximos_7_dias,

        (SELECT COUNT(*) FROM pruebas 
         WHERE DATE_TRUNC('month', fecha) = DATE_TRUNC('month', CURRENT_DATE)) as pruebas_este_mes,

        (SELECT COUNT(*) FROM controles 
         WHERE DATE_TRUNC('month', fecha) = DATE_TRUNC('month', CURRENT_DATE)) as controles_este_mes,

        (SELECT COUNT(*) FROM terrenos 
         WHERE DATE_TRUNC('month', fecha) = DATE_TRUNC('month', CURRENT_DATE)) as terrenos_este_mes

        """)

        row = cursor.fetchone()

        dashboard = {
            "pruebas_total": row[0],
            "controles_total": row[1],
            "terrenos_total": row[2],
            "pruebas_proximos_7_dias": row[3],
            "controles_proximos_7_dias": row[4],
            "terrenos_proximos_7_dias": row[5],
            "pruebas_este_mes": row[6],
            "controles_este_mes": row[7],
            "terrenos_este_mes": row[8]
        }

        cursor.close()
        conn.close()

        return dashboard
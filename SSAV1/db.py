import psycopg2
import yaml
import os

class  Acceso:
    def __init__(self,Funcion,Params = None):
        self.Funcion_ = Funcion
        self.Params_ = Params
        
    def get_db_connection():
        conn = psycopg2.connect(
            host="10.166.0.56",
            database="vacunacion_app",
            user="postgres",
            password="PMS2024"
        )
        return conn
    
    def EjecutaVista(self, condiciones=None):
        conn = Acceso.get_db_connection()
        try:
            cur = conn.cursor()
            where_clause = ""
            values = []
            if condiciones:
                where_parts = []
                for columna, (operador, valor) in condiciones.items():
                    if operador.upper() in ['IN', 'NOT IN']:
                        placeholders = ', '.join(['%s'] * len(valor))
                        where_parts.append(f"{columna} {operador} ({placeholders})")
                        values.extend(valor)
                    else:
                        where_parts.append(f"{columna} {operador} %s")
                        values.append(valor)
                where_clause = "WHERE " + " AND ".join(where_parts)
            query = f'SELECT * FROM {self.Funcion_} {where_clause}'
            cur.execute(query, values)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            data = [
                {column_name: row[idx] for idx, column_name in enumerate(column_names)}
                for row in rows
            ]
        finally:
            cur.close()
            conn.close()
        return data
    
    def EjecutaFuncion(self):
        conn = Acceso.get_db_connection()
        try:
            cur = conn.cursor()
            placeholders = ", ".join(["%s"] * len(self.Params_))
            query = f"SELECT * FROM {self.Funcion_}({placeholders})"
            cur.execute(query, self.Params_)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            data = [
                {column_name: row[idx] for idx, column_name in enumerate(column_names)}
                for row in rows
            ]
        finally:
            cur.close()
            conn.close()
        return data
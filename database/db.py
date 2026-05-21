import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect("database/cursos.db")
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS cursos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            descripcion TEXT,
            duracion TEXT

        )

        """)

        self.connection.commit()

    def add_course(self, titulo, descripcion, duracion):

        self.cursor.execute(
            """

        INSERT INTO cursos (titulo, descripcion, duracion)
        VALUES (?, ?, ?)

        """,
            (titulo, descripcion, duracion),
        )

        self.connection.commit()

    def get_courses(self):

        self.cursor.execute("SELECT * FROM cursos")

        return self.cursor.fetchall()

    def delete_course(self, course_id):

        self.cursor.execute("DELETE FROM cursos WHERE id = ?", (course_id,))

        self.connection.commit()

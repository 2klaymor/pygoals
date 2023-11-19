import core.shared.general
from core.repositories.base import SQLiteRepository


class TaskRepository(SQLiteRepository):
    def __init__(self):
        super().__init__(core.shared.general.TASKS)

        if not self.table_exists():
            self.create_table()

    def get_by_goal_id(self, goal_id_expr):
        cursor = self.conn.cursor()
        cursor.execute(
            f'SELECT * FROM {self.table} WHERE goal_id={goal_id_expr}',
        )
        return cursor.fetchall()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'CREATE TABLE Tasks ('
            '   id INTEGER PRIMARY KEY,'
            '   goal_id INTEGER NOT NULL,'
            '   text TEXT,'
            '   completed INTEGER,'
            '   FOREIGN KEY (goal_id) REFERENCES Goals (id)'
            '); '
        )

        self.conn.commit()

import core.shared.general
from core.repositories.base import SQLiteRepository


class GoalRepository(SQLiteRepository):
    def __init__(self):
        super().__init__(core.shared.general.GOALS)

        if not self.table_exists():
            self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'CREATE TABLE Goals ('
            '   id INTEGER PRIMARY KEY ,'
            '   name TEXT'
            '); '
        )

        self.conn.commit()


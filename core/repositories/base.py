import abc
import sqlite3

import core.shared.general


# Интерфейс репозитория
# Получение, создание, обновление, удаление
class IRepository(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_by_id(self, *args):
        pass

    @abc.abstractmethod
    def create(self, *args):
        pass

    @abc.abstractmethod
    def update(self, *args):
        pass

    @abc.abstractmethod
    def delete(self, *args):
        pass


# Реализация интерфейса конкретно для SQLite
class SQLiteRepository(IRepository):
    def __init__(self, table):
        self.table = table
        self.database_path = core.shared.general.data()
        self.conn = sqlite3.connect(self.database_path)

    def table_exists(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT name FROM sqlite_schema WHERE type=\'table\' AND name = ?',
            (self.table, )
        )

        return cursor.fetchone()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute(
            f'SELECT * FROM {self.table}',
        )
        return cursor.fetchall()

    def get_by_id(self, id_expr):
        cursor = self.conn.cursor()
        cursor.execute(
            f'SELECT * FROM {self.table} WHERE id={id_expr}'
        )
        return cursor.fetchone()

    def create(self, columns_expr, values_expr):
        cursor = self.conn.cursor()
        cursor.execute(
            f'INSERT INTO {self.table} {columns_expr} VALUES {values_expr}'
        )
        self.conn.commit()
        return self.get_by_id(cursor.lastrowid)

    def update(self, set_expr, where_expr):
        cursor = self.conn.cursor()
        cursor.execute(
            f'UPDATE {self.table} SET {set_expr} WHERE {where_expr}',
        )
        self.conn.commit()

    def delete(self, where_expr):
        cursor = self.conn.cursor()
        cursor.execute(
            f'DELETE FROM {self.table} WHERE {where_expr}'
        )
        self.conn.commit()

    def close(self):
        self.conn.close()

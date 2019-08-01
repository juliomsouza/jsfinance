from mysql.connector import connect as mysql_connect
from mysql.connector import Error as MysqlError
from decouple import config
from urllib.parse import urlparse


def dburl(url):
    u = urlparse(url)
    return dict(
        user=u.username,
        password=(u.password or ''),
        host=u.hostname,
        port=str(u.port),
        database=u.path[1:]
    )


def connect():
    return ConnectionAdapter(mysql_connect(**config('DATABASE_URL', cast=dburl)))


class ConnectionAdapter:
    def __init__(self, cnx):
        self._cnx = cnx

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is MysqlError:
            self._cnx.rollback()
        else:
            self._cnx.commit()

        self._cnx.close()

    def __getattr__(self, name):
        return getattr(self._cnx, name)


class DoesNotExist(Exception):
    pass


def category_get(id):
    with connect() as cnx:
        cursor = cnx.cursor()

        cursor.execute(f"SELECT * FROM CATEGORIAS WHERE ID_CAT = {id}")

        row = cursor.fetchone()

    if not row:
        raise DoesNotExist('Categoria não existe.')

    return row


def category_update(idcat, descricao):
    with connect() as cnx:
        cursor = cnx.cursor()
        sql = f"UPDATE CATEGORIAS SET DESC_CAT = '{descricao}' WHERE ID_CAT = {idcat}"

        cursor.execute(sql)


def category_insert(descricao, obs):
    with connect() as cnx:
        # retornar o id criado.
        cursor = cnx.cursor()
        cursor.execute(f"INSERT INTO CATEGORIAS (DESC_CAT, OBS_CAT) "
                       f"VALUES ('{descricao}', '{obs}')")


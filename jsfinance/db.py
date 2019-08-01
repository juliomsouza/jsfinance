from mysql.connector import connect as mysql_connect
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
        self._cnx.close()

    def __getattr__(self, name):
        return getattr(self._cnx, name)

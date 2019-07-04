from mysql.connector import connect as mysql_connect
from decouple import config


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
    return mysql_connect(**config('DATABASE_URL', cast=dburl))


import pathlib

from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret

config_path = pathlib.Path(__file__).parent.absolute() / ".env"
config = Config(str(config_path))

TESTING = config("TESTING", cast=bool, default=False)

DB_DRIVER = config("DB_DRIVER", default="postgresql")
DB_HOST = config("DB_HOST", default='127.0.0.1')
DB_PORT = config("DB_PORT", cast=int, default=5432)
DB_USER = config("DB_USER", default='username')
DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default='password')
DB_DATABASE = config("DB_DATABASE", default='default_company')
DB_DSN = config(
    "DB_DSN",
    cast=make_url,
    default=URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    ),
)

BOT_ID = config("BOT_ID")
APP_ID = config("APP_ID")

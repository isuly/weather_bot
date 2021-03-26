from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from app import config

pool_engine = create_engine(
    config.DB_DSN,
    poolclass=QueuePool,

)
SessionPool = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=True, bind=pool_engine)


class SessionPoolContext:
    """Открытие сессии через контекстный менеджер with"""

    def __enter__(self):
        self.session = SessionPool()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

from sqlalchemy import Column, Boolean, String, Integer, DateTime
import datetime
from app.db import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {
        'comment': 'Таблица пользователей.'
    }
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True),
                        default=datetime.datetime.utcnow,
                        index=False, nullable=False)
    username = Column(String())
    city = Column(String())
    is_active = Column(Boolean())


__all__ = User
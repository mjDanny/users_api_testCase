from sqlalchemy import Column, String, Enum, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import UUID
import uuid

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    avatar = Column(String, nullable=True)
    gender = Column(Enum('male', 'female', name='gender_types'), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    __table_args__ = (
        UniqueConstraint('email', name='uq_client_email'),
    )
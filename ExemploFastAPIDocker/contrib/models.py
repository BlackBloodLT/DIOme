from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_columm
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_columm(PD_UUID(as_uuid=True), default=uuid4, nullable=False)
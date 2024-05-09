from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
import ExemploFastAPIDocker.contrib.models import BaseModel

class AtletaModel():
    __tablename__ = 'Atleta'

    pk_id: Mapped[int] = mapped_columm(Integer, primary_key=True)
    nome: Mapped[str] = mapped_columm(String(50), nullable=False)
    cpf: Mapped[str] = mapped_columm(String(11), nullable=False)
    idade: Mapped[int] = mapped_columm(Integer, nullable=False)
    peso: Mapped[float] = mapped_columm(Float, nullable=False)
    altura: Mapped[float] = mapped_columm(Float, nullable=False)
    sexo: Mapped[str] = mapped_columm(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_columm(Datetime, nullable=False)

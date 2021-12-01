from sqlalchemy.orm import relationship, validates
from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime
import re
from app.exceptions.exc import CpfFormatError
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class MotoristaModel(db.Model):
  nome: str
  sobrenome: str
  cpf: str
  created_at: str
  cnh: str
  updated_at: str
  localizacao: str
  
  __tablename__ = 'motoristas'
  
  id = Column(Integer, primary_key=True)
  nome = Column(String, nullable=False)
  sobrenome = Column(String, nullable=False)
  password_hash = Column(String(255), nullable=False)
  cpf = Column(String, nullable=False, unique=True)
  created_at = Column(DateTime)
  cnh = Column(String(11), nullable=False, unique=True)
  updated_at = Column(DateTime)
  localizacao = Column(String)
  
  caminhoes = relationship('CaminhaoModel', backref='motorista', uselist=False)

  @validates('cpf')
  def valida_cpf(self, key, cpf):
    pattern = "(^\d{3}\.\d{3}\.\d{3}\-\d{2}$)"

    if not re.search(pattern, cpf):
      raise CpfFormatError("Formato de CPF inválido. Formato aceito = xxx.xxx.xxx-xx")

    return cpf
  
  @property
  def password(self):
    raise AttributeError("Password cannot be acessed!")
  
  @password.setter
  def password(self, password_to_hash):
    self.password_hash = generate_password_hash(password_to_hash)
  
  def verify_password(self, password_to_compare):
    return check_password_hash(self.password_hash, password_to_compare)
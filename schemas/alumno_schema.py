from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

from schemas.asistente_schema import AsistenteOut
from schemas.evaluacion_schema import EvaluacionOut
from schemas.pregunta_schema import PreguntaOut
from schemas.thread_schema import ThreadOut

# Schema base con los campos comunes
class AlumnoBase(BaseModel):
    email: EmailStr
    firebase_uid: Optional[str] = None
    contrasena: str
    
class AlumnoCreate(AlumnoBase):
    pass

class AlumnoUpdate(BaseModel):
    email: Optional[EmailStr] = None
    firebase_uid: Optional[str] = None
    contrasena: Optional[str] = None
    
class AlumnoOut(AlumnoBase):
    id: int
    last_login: datetime
    asistentes: List[AsistenteOut] = []
    preguntas: List[PreguntaOut] = []
    evaluaciones: List[EvaluacionOut] = []
    threads: List[ThreadOut] = []
    
    class Config:
        orm_mode = True
from typing import Optional
from datetime import DateTime
from pydantic import BaseModel
#User Model
class User(BaseModel): #Schema
     id:int
     nombre:str
     apellido:str
     direccion:Optional[str]
     Telefono:int
     correo:str
     cracion:DateTime = DateTime.now()

class UserId(BaseModel):
    id:int
from fastapi import APIRouter,Depends
from app.schemas import User,UserId
from app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios = []

@router.get('/ruta1')
def ruta1():
    return {"mensaje":"Prueba de apifast"}

@router.get('/')
def obtener_usuarios(db:Session = Depends(get_db)):
    return usuarios
    # return usuarios

@router.post("/")
def crear_usuario(user:User):
     usuario = user.dict()
     usuarios.append(usuario)
     print(usuario)
     return {"respuesta":"Usuario creado satisfactoriamente"}

@router.post('//{user_id}')
def obtener_usuarios(user_id:int):
    for user in usuarios:
        if user["id"] == user_id:
          return {"usuario":user}
    return {"respuesta":"usuario no encontrado"}

@router.post('/obtener_usuario2')
def obtener_usuario_2(user_id:UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
          return {"usuario":user}
    return {"respuesta":"usuario no encontrado"}

@router.delete('//{user_id}')
def eliminar_usuario(user_id:int):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios.pop(index)
            return {"mensaje":"Usuario eliminado correctamente"}
        return {"mensaje":"Usuario no encontrado"}
    

@router.put('//{user_id}')
def actualizar_usuario(user_id:int ,updateUser:User ):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
             usuarios[index]["id"] = updateUser.dict()["id"]
             usuarios[index]["nombre"] = updateUser.dict()["nombre"]
             usuarios[index]["apellido"] = updateUser.dict()["apellido"]
             usuarios[index]["direccion"] = updateUser.dict()["direccion"]
             usuarios[index]["Telefono"] = updateUser.dict()["Telefono"]
             return {"mensaje":"Usuario actualizado correctamente"}
        return {"mensaje":"Usuario no encontrado"}
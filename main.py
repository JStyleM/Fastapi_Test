from fastapi import FastAPI, Depends, status, HTTPException
from schemas import Usuarios, UsuariosCreate, UsuariosResponse
from data import get_session


app = FastAPI()



@app.get("/usuarios", response_model=list[UsuariosResponse], status_code=status.HTTP_200_OK)
def listar_Usuarios(db = Depends(get_session)):
    """
    Lista todos los usuarios de la base de datos.
    """
    try:
        # Realizar la consulta para obtener todos los usuarios
        usuarios = db.query(Usuarios).all()


        # Validar si no hay usuarios en la base de datos
        if not usuarios:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No se encontraron usuarios en la base de datos."
            )

        return usuarios

    except HTTPException as http_exc:
        # Re-lanzar excepciones HTTP personalizadas
        raise http_exc

    except Exception as e:
        # Manejo genérico de errores
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al listar los usuarios: {str(e)}"
        )



@app.post("/usuarios", response_model=Usuarios, status_code=status.HTTP_201_CREATED)
def crear_Usuarios(usuario: UsuariosCreate, db = Depends(get_session)):
    """
    Crea un nuevo usuario en la base de datos.
    """
    try:

        nuevo_usuario = Usuarios(**usuario.model_dump())

        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

    except Exception as e:

        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error al Crear el Usuario: {str(e)}',
        )

    return nuevo_usuario



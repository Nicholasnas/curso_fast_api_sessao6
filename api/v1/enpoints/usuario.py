from typing import List, Optional, Any
from fastapi import (
    APIRouter, status, HTTPException, Depends, Response
)
from fastapi.security import OAuth2PasswordRequestForm # identificar que alguns endpoints precisade auth
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.usuario_model import UsuarioModel
from schemas.usuario_schema import (
    UsuarioSchemaBase,UsuarioSchemaCreate,
    UsuarioSchemaArtigos,UsuarioSchemaUp
)
from core.security import gerar_hash_senha
from core.deps import get_current_user,get_session
from core.auth import autenticar, criar_token_acesso


router = APIRouter()


# GET logado
@router.get('/logado', response_model=UsuarioSchemaBase)
def get_logado(usuario_logado:UsuarioModel=Depends(get_current_user)):
    return usuario_logado

# post/ signup criar a conta do usuario
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemaBase)
async def post_usuario(usuario:UsuarioSchemaCreate, db:AsyncSession=Depends(get_session)):
    new_user: UsuarioModel = UsuarioModel(
        nome=usuario.nome, email=usuario.email, 
        senha=gerar_hash_senha(usuario.senha), eh_admin=usuario.eh_admin
    )
    async with db as session:
        session.add(new_user)
        await session.commit()
        return new_user
    
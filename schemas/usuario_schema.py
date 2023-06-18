from typing import Optional, List
from pydantic import BaseModel, EmailStr
from schemas.artigo_schema import ArtigoSchema

# nao retorna senha
class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class Config:
        orm_mode = True

# Usado para criar a conta
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

#  usuario mais artigos
class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]

# atualizar dados, alterar no minimo um atributo
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]


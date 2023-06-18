from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Cursos API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ =="__main__":
    import uvicorn
    uvicorn.run('main:app', port=5000,
                log_level='info', reload=True)
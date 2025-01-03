from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.infraestructure.db.db import get_db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from app.security.autenticationJWT import validateToken
from app.interfaces.controllers.loginController import router as loginRouter

app=FastAPI()

class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        if data['username'] != 'admin':
            HTTPException(status_code=403, detail="Invalid username or password")


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Realizamos una consulta simple para verificar la conexión
        result = db.execute(text("SELECT 1"))
        return {"status": "ok", "detail": "Database connection is healthy"}
    except SQLAlchemyError as e:
        # En caso de error con la base de datos
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Registrar las rutas
app.include_router(loginRouter)
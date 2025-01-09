from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infraestructure.db.db import get_db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from app.interfaces.controllers.loginController import router as loginRouter
from app.interfaces.controllers.accountsController import router as accountRouter
from app.interfaces.controllers.inventoryController import router as inventoryRouter
from app.interfaces.controllers.itemInventoryController import router as itemInventoryRouter

app=FastAPI()

# Registrar las rutas
app.include_router(loginRouter)
app.include_router(accountRouter)
app.include_router(inventoryRouter)
app.include_router(itemInventoryRouter)

# @app.get("/health")
# def health_check(db: Session = Depends(get_db)):
#     try:
#         # Realizamos una consulta simple para verificar la conexión
#         result = db.execute(text("SELECT 1"))
#         return {"status": "ok", "detail": "Database connection is healthy"}
#     except SQLAlchemyError as e:
#         # En caso de error con la base de datos
#         raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

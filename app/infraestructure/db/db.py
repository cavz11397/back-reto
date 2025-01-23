from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from app.config.settings import DATABASE_URL

# Crea el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Crea una clase de sesión que se utilizará para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una clase base para las definiciones de modelos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
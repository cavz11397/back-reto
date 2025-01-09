import jwt 
from app.config.settings import SECRET_KEY

def createToken(data: dict):
    token: str = jwt.encode(payload=data, key=SECRET_KEY, algorithm='HS256')
    return token

def validateToken(token: str) -> dict:
    data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return data
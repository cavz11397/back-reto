from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from app.security.autenticationJWT import validateToken

class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        if data['username'] != 'admin':
            HTTPException(status_code=403, detail="Invalid username or password")
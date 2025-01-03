import jwt 

def createToken(data: dict):
    token: str = jwt.encode(payload=data, key='secret', algorithm='HS256')
    return token

def validateToken(token: str) -> dict:
    data = jwt.decode(token, 'secret', algorithms=['HS256'])
    return data
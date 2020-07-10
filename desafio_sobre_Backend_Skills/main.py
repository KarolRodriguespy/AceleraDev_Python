import jwt
from jwt import DecodeError

secret = 'acelera'

data = {
    "language": "Python"
}

def create_token(data, secret):

   try:
    token = jwt.encode(data, secret, algorithm='HS256')
    return token
   except:
       return {'error': 1}

def verify_signature(token):

    try:
        content = jwt.decode(token, secret, algorithms='HS256')
        return content
    except DecodeError:
        return {"error": 2}


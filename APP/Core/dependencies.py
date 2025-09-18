from fastapi import Header, HTTPException
from APP.Core.config import settings 
from APP.Core.security import verify_token



def get_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail='Inavalid API key')
    

def get_current_user(token: str = Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Invalid JWT Token')
    return payload


    

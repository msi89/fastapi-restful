from fastapi import Header, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from accounts.models import User
from core.contrib.security import verify_password
from core import settings
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def authenticate(username: str, password: str) -> User:
    user = await User.get(email=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


async def get_auth_user(token: str = Depends(oauth2_scheme)) -> User:

    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise HTTPException(status_code=400, detail="Bad credentials")
    except JWTError:
        raise HTTPException(status_code=400, detail="Bad credentials")
    user = await User.get(email=email)
    if user is None:
        raise HTTPException(status_code=400, detail="Not authorized")
    return user


async def get_active_user(current_user: User = Depends(get_auth_user)) -> User:
    if current_user.is_active:
        return current_user
    return HTTPException(status_code=400, detail="Inactive user")


async def get_super_user(current_user: User = Depends(get_auth_user)) -> User:
    if current_user.is_superuser:
        return current_user
    raise HTTPException(status_code=400, detail="You are not super user")


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

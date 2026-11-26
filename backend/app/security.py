from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import get_db
from app.models import User

settings = get_settings()

# auto_error=False: if the header is missing, FastAPI will NOT reject it for us.
# We raise the 401 ourselves so the status code and message are under our control.
bearer_scheme = HTTPBearer(auto_error=False)


def hash_password(password: str) -> str:
    # .encode("utf-8") to go to bytes, .decode("utf-8") to come back.
    bytes_pass = password.encode("utf-8")
    result = bcrypt.hashpw(bytes_pass, bcrypt.gensalt())
    decoded_pass = result.decode("utf-8")
    return decoded_pass


def verify_password(password: str, hashed_password: str) -> bool:
    password_encoded = password.encode("utf-8")
    hashed_password_encoded = hashed_password.encode("utf-8")
    result = bcrypt.checkpw(password_encoded, hashed_password_encoded)
    return result


def create_access_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc)
        + timedelta(minutes=settings.access_token_expire_minutes),
    }
    final_token = jwt.encode(
        payload, settings.secret_key, algorithm=settings.jwt_algorithm
    )
    return final_token


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    raised_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not Authenticated!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if credentials is None:
        raise raised_error

    try:
        data = jwt.decode(
            credentials.credentials,
            settings.secret_key,
            algorithms=[settings.jwt_algorithm],
        )
    except jwt.InvalidTokenError:
        raise raised_error

    user_id = int(data["sub"])
    user = db.get(User, user_id)
    if user is None:
        raise raised_error
    else:
        return user

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
    # TODO: bcrypt.hashpw(password_as_bytes, bcrypt.gensalt()) returns bytes; return it as a str.
    #   hint: .encode("utf-8") to go to bytes, .decode("utf-8") to come back.
    ...


def verify_password(password: str, hashed_password: str) -> bool:
    # TODO: bcrypt.checkpw(password_bytes, hashed_bytes) -> bool
    ...


def create_access_token(user_id: int) -> str:
    # TODO: build a payload dict with
    #   "sub": str(user_id)   (PyJWT requires the subject to be a STRING)
    #   "exp": now (UTC) + timedelta(minutes=settings.access_token_expire_minutes)
    #   then jwt.encode(payload, settings.secret_key, algorithm=settings.jwt_algorithm)
    #   hint: datetime.now(timezone.utc)
    ...


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    # TODO: 1. If credentials is None -> raise 401.
    #       2. Decode: jwt.decode(credentials.credentials, settings.secret_key, algorithms=[settings.jwt_algorithm])
    #          Always pass algorithms as a LIST. Catch jwt.InvalidTokenError (covers bad signature AND expired) -> 401.
    #       3. user_id = int(payload["sub"]); load the user with db.get(User, user_id).
    #          If the user does not exist (deleted account) -> 401.
    #       4. Return the user.
    #   One 401 helper is cleaner than repeating the raise:
    #   HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated",
    #                 headers={"WWW-Authenticate": "Bearer"})
    ...

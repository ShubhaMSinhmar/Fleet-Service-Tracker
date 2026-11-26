from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import LoginRequest, RegisterRequest, TokenResponse, UserRead
from app.security import (
    create_access_token,
    get_current_user,
    hash_password,
    verify_password,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)) -> User:
    # TODO 1: look for an existing user with this email:
    #   db.scalar(select(User).where(User.email == payload.email))
    #   if found -> raise HTTPException(409, "Email already registered")
    # TODO 2: create User(email=..., full_name=..., hashed_password=hash_password(payload.password))
    # TODO 3: db.add(user); db.commit(); db.refresh(user); return user
    # BONUS: two requests at the same moment can both pass the check in TODO 1.
    #   Wrap commit in try/except IntegrityError: db.rollback() and raise the same 409.
    ...


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> TokenResponse:
    # TODO: find the user by email. If there is no user OR verify_password fails,
    #   raise the SAME 401 with the SAME message ("Invalid email or password").
    #   Why the same? So an attacker cannot learn which emails are registered.
    # Then return TokenResponse(access_token=create_access_token(user.id))
    ...


@router.get("/me", response_model=UserRead)
def me(current_user: User = Depends(get_current_user)) -> User:
    # TODO: return the current user. (One line: get_current_user already did the work.)
    ...

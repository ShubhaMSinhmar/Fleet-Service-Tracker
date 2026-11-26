from email.policy import default
import re
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def normalize_email(value: str) -> str:
    # TODO: strip spaces, make it lowercase, and raise ValueError("Invalid email address")
    #   if it does not match EMAIL_PATTERN. Return the cleaned email.
    #   Why lowercase? So "A@x.com" and "a@x.com" cannot become two accounts.
    if EMAIL_PATTERN.match(value):
        return value.strip(" ").lower()
    else:
        raise ValueError("Invalid email address!")


def check_password_bytes(value: str) -> str:
    # TODO: bcrypt only accepts up to 72 BYTES (not characters; "é" is 2 bytes).
    #   If len(value.encode("utf-8")) > 72 raise ValueError("Password is too long"), else return value.
    if len(value.encode("utf-8")) > 72:
        raise ValueError("Password is too long!")
    else:
        return value


class RegisterRequest(BaseModel):
    # TODO fields: email (str), full_name (str, 1 to 100 chars), password (str, 8 to 72 chars)
    #   hint: full_name: str = Field(min_length=1, max_length=100)
    email: str = Field()
    full_name: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=8, max_length=72)
    # TODO validators (run on the field value):
    #   @field_validator("email") + @classmethod -> return normalize_email(value)
    #   @field_validator("password") + @classmethod -> return check_password_bytes(value)


class LoginRequest(BaseModel):
    # TODO fields: email (str), password (str, 1 to 72 chars)
    email: str = Field()
    password: str = Field(min_length=1, max_length=72)
    # TODO validators: same two as RegisterRequest


class UserRead(BaseModel):
    # TODO fields: id (int), email (str), full_name (str), created_at (datetime)
    id: int = Field()
    email: str = Field()
    full_name: str = Field()
    created_at: datetime = Field()
    # TODO: model_config = ConfigDict(from_attributes=True)
    #   so pydantic can read a SQLAlchemy User object (attributes) and not only dicts.


class TokenResponse(BaseModel):
    # TODO fields: access_token (str), token_type (str, default "bearer")
    access_token: str = Field()
    token_type: str = Field(default="bearer")

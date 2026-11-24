from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    # Pattern example: a unique, indexed string column
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    # TODO: full_name (String 100), hashed_password (String 255)
    # TODO: created_at -> Mapped[datetime], DateTime(timezone=True), server_default=func.now()
    # TODO: cars -> Mapped[list["UserCar"]] = relationship(back_populates="user")


class CarModel(Base):
    __tablename__ = "car_models"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    # TODO: body_type (String 50), image_url (String 500)
    # TODO: service_interval_months (int), service_interval_km (int)
    # TODO: base_parts_cost, base_labour_cost -> Mapped[Decimal], Numeric(10, 2)


class UserCar(Base):
    __tablename__ = "user_cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    # Pattern example: a foreign key (indexed, because we filter by it on every query)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    # TODO: car_model_id -> ForeignKey("car_models.id")
    # TODO: nickname (String 100), registration_year (int)
    # TODO: vin (String 17, unique)
    # TODO: current_mileage_km (int), last_service_mileage_km (int)
    # TODO: last_service_date -> Mapped[date], Date
    # TODO: created_at (same as User)
    # TODO: relationships: user -> "User" (back_populates="cars"), car_model -> "CarModel"

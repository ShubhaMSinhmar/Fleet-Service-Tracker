from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    cars: Mapped[list["UserCar"]] = relationship(back_populates="user")


class CarModel(Base):
    __tablename__ = "car_models"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    body_type: Mapped[str] = mapped_column(String(50))
    image_url: Mapped[str] = mapped_column(String(500))
    service_interval_months: Mapped[int] = mapped_column(Integer)
    service_interval_km: Mapped[int] = mapped_column(Integer)
    base_parts_cost: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    base_labour_cost: Mapped[Decimal] = mapped_column(Numeric(10, 2))


class UserCar(Base):
    __tablename__ = "user_cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    car_model_id: Mapped[int] = mapped_column(ForeignKey("car_models.id"), index=True)
    nickname: Mapped[str] = mapped_column(String(100))
    registration_year: Mapped[int] = mapped_column(Integer)
    vin: Mapped[str] = mapped_column(String(17), unique=True)
    current_mileage_km: Mapped[int] = mapped_column(Integer)
    last_service_mileage_km: Mapped[int] = mapped_column(Integer)
    last_service_date: Mapped[date] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    user: Mapped["User"] = relationship(back_populates="cars")
    car_model: Mapped["CarModel"] = relationship()

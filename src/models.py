from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

db = SQLAlchemy()

user_planet = Table(
    'user_table',
    db.Model.metadata,
    db.Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    db.Column('planet_id', Integer, ForeignKey('planets.id_planet'), primary_key=True),
)

class Species(db.Model):
    __tablename__ = 'species'

    id_specie: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_specie: Mapped[str] = mapped_column(String(50), nullable=False)
    language: Mapped[str] = mapped_column(String(50), nullable=False)

    def serialize(self):
        return {
            "id_specie": self.id_specie,
            "name_specie": self.name_specie,
            "language": self.language
        }

class Vehicles(db.Model):
    __tablename__ = 'vehicles'

    id_vehicle: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_vehicle: Mapped[str] = mapped_column(String(50), nullable=False)
    passengers: Mapped[int] = mapped_column(Integer, nullable=True)

    def serialize(self):
        return {
            "id_vehicle": self.id_vehicle,
            "name_vehicle": self.name_vehicle,
            "passenger": self.passengers
        }

class Planets(db.Model):
    __tablename__ = 'planets'

    id_planet: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_planet: Mapped[str] = mapped_column(String(100), nullable=False)
    diameter: Mapped[int] = mapped_column(Integer, nullable=True)
    gravity: Mapped[int] = mapped_column(Integer, nullable=True)

    planet_specie: Mapped[Optional[int]] = mapped_column(ForeignKey("species.id_specie"), nullable=True)
    planet_vehicle: Mapped[Optional[int]] = mapped_column(ForeignKey("vehicles.id_vehicle"), nullable=True)

    def serialize(self):
        return {
            "id_planet": self.id_planet,
            "name_planet": self.name_planet,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "planet_specie": self.planet_specie,
            "planet_vehicle": self.planet_vehicle
        }

class Peoples(db.Model):
    __tablename__ = 'peoples'

    id_people: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_people: Mapped[str] = mapped_column(String(100), nullable=False)

    id_homeworld: Mapped[Optional[int]] = mapped_column(ForeignKey("planets.id_planet"))
    specie_people: Mapped[Optional[int]] = mapped_column(ForeignKey("species.id_specie"))
    vehicle_people: Mapped[Optional[int]] = mapped_column(ForeignKey("vehicles.id_vehicle"))

    def serialize(self):
        return {
            "id_people": self.id_people,
            "name_people": self.name_people,
            "id_homeworld": self.id_homeworld,
            "specie_people": self.specie_people,
            "vehicle_people": self.vehicle_people
        }
     
class User(db.Model):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

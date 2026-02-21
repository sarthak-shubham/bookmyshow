from database import engine, Base

from models.user import User
from models.movie import Movie
from models.theatre import Theatre
from models.screen import Screen
from models.seat import Seat
from models.show import Show
from models.booking import Booking
from models.booking_seat import BookingSeat

Base.metadata.create_all(bind=engine)
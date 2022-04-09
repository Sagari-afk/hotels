from random import choice, randint

from django.db import IntegrityError

from hotel_app.models import (
    City,
    Hotel,
    Room,
    Booking,
)
from hotel_app.utils.constants import (
    CITIES,
    LETTERS
)


def create_cities():
    cities = [City(title=city) for city in CITIES]
    try:
        City.objects.bulk_create(cities)
    except IntegrityError:
        print(f"{cities}: come of cities already exists")


def create_hotels():
    cities = City.objects.all()
    hotels = [Hotel(title=f"Hotel_{letter}" for letter in LETTERS)]
    for hotel in hotels:
        hotel.city = choice(cities)
        try:
            hotel.save()
            hotel_rooms_amount = randint(100, 1000)
            create_room(hotel, hotel_rooms_amount)
        except IntegrityError:
            print(f"{hotel}: already exists in the {hotel.city}")


def create_room(hotel, hotel_rooms_amount):
    hotels = Hotel.objects.all()
    rooms = [Room(room_number=randint(0, 1000), beds=randint(1, 4), hotel=h) for h in hotels]
    try:
        Room.objects.bulk_create(rooms)
    except IntegrityError:
        print(f"This room already exists")


# 1. create_room logic
# 2. urls + view to show all awailable hotels in db

from django.db import models


class City(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title


class Hotel(models.Model):
    title = models.CharField(max_length=50)
    city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        related_name="hotels",
    )

    class Meta:
        unique_together = "title", "city"

    def __str__(self):
        return f"{self.city}:{self.title}"


class Room(models.Model):
    room_number = models.IntegerField()
    beds = models.IntegerField()
    hotel = models.ForeignKey(
        "Hotel",
        on_delete=models.CASCADE,
        related_name="rooms",
    )

    class Meta:
        unique_together = "room_number", "hotel"


class Booking(models.Model):
    guest_name = models.CharField(max_length=120)
    persons = models.IntegerField()
    booking_start = models.DateField()
    booking_end = models.DateField()
    price = models.FloatField()
    room = models.ForeignKey(
        "Room",
        on_delete=models.CASCADE,
        related_name="bookings"
    )

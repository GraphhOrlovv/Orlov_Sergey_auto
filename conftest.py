import pytest

from clients.booking_client import BookingClient
from models.booking import Booking, BookingDates
from src.constant import BookingData

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture
def booking_client(): # инициализация клиента
    return BookingClient(baseurl=BASE_URL)

@pytest.fixture
def valid_booking_payload():
    return Booking(
        firstname=BookingData.FIRSTNAME.value,
        lastname=BookingData.LASTNAME.value,
        totalprice=1000,
        depositpaid=True,
        bookingdates=BookingDates(
            checkin="2027-01-01",
            checkout="2027-01-01"
        ),
        additionalneeds="Breakfast"
    )

@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}

@pytest.fixture
def created_booking(booking_client, valid_booking_payload, headers):
    response = booking_client.create_booking(valid_booking_payload.build(), headers)
    data = response.json()
    yield data
    booking_client.delete_booking(data['bookingid'], headers)
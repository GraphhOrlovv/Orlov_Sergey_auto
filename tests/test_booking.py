from pprint import pprint

from models.booking import CreateBookingResponse
from src.constant import BookingData


def test_create_booking(created_booking):
    try:
        parsed = CreateBookingResponse(**created_booking)
    except Exception as e:
        raise AssertionError(f"Структура ответа не соответствует данным: {e}")

    assert parsed.booking.bookingdates.checkin == "2027-01-01"

    assert created_booking['booking']['firstname'] == BookingData.FIRSTNAME.value, (
        "Вернулось некорректное имя\n"
        f"Response:\n{created_booking}\n"
        f"Ожидаемое имя: {BookingData.FIRSTNAME.value}"
    )
    assert created_booking['booking']['lastname'] == BookingData.LASTNAME.value, (
        "Вернулось некорректная фамилия\n"
        f"Response:\n{created_booking}\n"
        f"Ожидаемое имя: {BookingData.LASTNAME.value}"
    )
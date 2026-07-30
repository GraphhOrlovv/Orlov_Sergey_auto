import allure
import requests

from src.settings import settings


class BookingClient:
    def __init__(self, baseurl):
        self.baseurl = baseurl

    @allure.step("Создание брони")
    def create_booking(self, data: dict, headers: dict) -> requests.Response:
        return requests.post(url=f"{self.baseurl}/booking", json=data, headers=headers)

    @allure.step("Удаление брони")
    def delete_booking(self, booking_id: int, headers: dict) -> requests.Response:
        return requests.delete(
            f"{self.baseurl}/booking/{str(booking_id)}", headers=headers
        )

    @allure.step("Получение токена")
    def get_token(self) -> requests.Response:
        return requests.post(
            f"{self.baseurl}/auth",
            json={"username": settings.user_name, "password": settings.password},
        )

    @allure.step("Обновление брони")
    def update_booking(self, booking_id: int, headers: dict, data) -> requests.Response:
        return requests.put(
            f"{self.baseurl}/booking/{str(booking_id)}", headers=headers, json=data
        )

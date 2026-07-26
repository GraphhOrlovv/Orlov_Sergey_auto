import requests

class BookingClient:
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def create_booking(self, data: dict, headers: dict) -> requests.Response:
        return requests.post(url=f"{self.baseurl}/booking", json=data, headers=headers)

    def delete_booking(self, booking_id: int, headers: dict) -> requests.Response:
        return requests.delete(f"{self.baseurl}/booking/{str(booking_id)}", headers=headers)
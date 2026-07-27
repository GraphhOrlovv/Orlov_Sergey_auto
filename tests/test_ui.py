from time import sleep

from pages.home_page import HomePage


def test_add_to_cart(page, base_url):
    home_page = HomePage(page, base_url)
    home_page.open()
    home_page.go_to_products()

    sleep(3)

from pages.base_page import BasePage


class HomePage(BasePage):
    PRODUCT_LINK = 'a[href="/products"]'

    def open(self):
        self.goto(wait_until="commit")
        self.page.wait_for_load_state("domcontentloaded")
        # Проверяем, что подгрузилась структура страницы

    def go_to_products(self):
        self.page.click(self.PRODUCT_LINK)

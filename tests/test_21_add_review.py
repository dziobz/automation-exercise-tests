from playwright.sync_api import Page, expect
from models.products import ProductPage


def test_search_products_and_verify_cart_after_login(page: Page):

    home = ProductPage(page)
    home.products()
    home.write_review(1)
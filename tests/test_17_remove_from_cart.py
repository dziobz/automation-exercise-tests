from playwright.sync_api import Page
from models.homepage import Homepage
import json


def test_remove_products_from_cart(page: Page):

    homepage = Homepage(page)
    homepage.add_to_cart(1)
    homepage.add_to_cart(2)
    homepage.go_to_cart()
    homepage.remove_from_cart()
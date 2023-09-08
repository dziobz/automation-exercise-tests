from playwright.sync_api import Page
from models.homepage import Homepage


def test_add_to_cart_from_recomemended_items(page: Page):
    homepage = Homepage(page)

    homepage.add_to_cart_recommended()
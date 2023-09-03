from playwright.sync_api import Page, expect
from models.products import ProductPage


def test_view_and_cart_brand_products(page: Page):

    brands_page = ProductPage(page)
    brands_page.verify_brands("Biba")
    brands_page.verify_brands("Polo")
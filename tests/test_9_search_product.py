from playwright.sync_api import Page, expect
import pytest
from models.products import ProductPage


def test_search_products(page: Page):

    products_page = ProductPage(page)
    products_page.products()
    product_name = "Top"
    products_page.search_product(product_name)

from playwright.sync_api import Page, expect
import pytest
from models.products import ProductPage


def test_all_products(page: Page):
    # arrive at Products page
    product_page = ProductPage(page)
    product_page.products()
    # check if first product is visible, click on it
    expect(product_page.page.locator("//a[@href='/product_details/1']")).to_be_visible()
    product_page.page.locator("//a[@href='/product_details/1']").click()
    expect(product_page.page).to_have_url("https://www.automationexercise.com/product_details/1")
    # check if product details are visible
    expect(product_page.page.locator("div.product-information")).to_be_visible()
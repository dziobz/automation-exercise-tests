from playwright.sync_api import Page, expect
from models.products import ProductPage


def test_search_products_and_verify_cart_after_login(page: Page):

    product = "White Top"
    home = ProductPage(page)
    home.products()
    home.search_product(product)
    home.add_to_cart(1)
    home.go_to_cart()

    chck = home.page.locator("table#cart_info_table")
    expect(chck).to_contain_text(product)
    home.page.locator("//a[contains(text(),'Signup / Login')]").click()
    home.login("dziobzi2137@gmail.com", "123456789")

    home.go_to_cart()
    expect(chck).to_contain_text(product)
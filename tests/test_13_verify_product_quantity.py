from playwright.sync_api import Page, expect
from models.products import ProductPage


def test_product_quantity(page: Page):

    products_page = ProductPage(page)
    view_first_product = products_page.page.locator("//a[@href='/product_details/1']")
    view_first_product.click()

    expect(page).to_have_url("https://www.automationexercise.com/product_details/1")
    quantity = products_page.page.locator("input#quantity")
    quantity.dblclick()
    quantity.fill("4")

    add_to_cart = products_page.page.get_by_role("button", name="Add to cart")
    add_to_cart.click()

    view_cart = products_page.page.locator("//u[contains(text(),'View Cart')]")
    view_cart.click()
    
    checkout = products_page.page.get_by_role("rowgroup")
    first_row = checkout.locator("tr#product-1")
    expect(first_row).to_be_visible()
    expect(first_row.locator("td.cart_quantity")).to_contain_text("4")

from playwright.sync_api import Page, expect
from models.products import ProductPage

def test_add_to_cart(page: Page):
    
    products_page = ProductPage(page)
    products_page.products()

    first_product = products_page.page.locator("div.single-products").nth(0)
    first_price = first_product.locator("div.overlay-content h2").inner_text()
    first_product.hover()
    products_page.page.locator("a.btn.btn-default.add-to-cart").nth(0).click()
    continue_btn = products_page.page.locator("button.btn.btn-success.close-modal")
    continue_btn.click()

    second_product = products_page.page.locator("div.single-products").nth(1)
    second_price = second_product.locator("div.overlay-content h2").inner_text()
    second_product.hover()
    products_page.page.locator("div:nth-child(4) > .product-image-wrapper > .single-products > .product-overlay > .overlay-content > .btn").click()
    
    view_cart = products_page.page.locator("//u[contains(text(),'View Cart')]")
    view_cart.click()

    checkout = products_page.page.get_by_role("rowgroup")
    first_row = checkout.locator("tr#product-1")
    second_row = checkout.locator("tr#product-2")
    expect(first_row).to_be_visible()
    expect(second_row).to_be_visible()
    
    expect(first_row.locator("td.cart_price")).to_contain_text(first_price)
    expect(second_row.locator("td.cart_price")).to_contain_text(second_price)

    expect(first_row.locator("td.cart_quantity")).to_contain_text("1")
    expect(second_row.locator("td.cart_quantity")).to_contain_text("1")

    expect(first_row.locator("td.cart_total")).to_have_text(first_price)
    expect(second_row.locator("td.cart_total")).to_have_text(second_price)
from playwright.sync_api import Page, expect
from models.homepage import Homepage


def test_view_category_products(page: Page):

    homepage = Homepage(page)
    categories = homepage.page.locator("div#accordian")
    expect(categories).to_be_visible()

    women = homepage.page.locator("a[href='#Women']")
    women.click()
    women_dress = homepage.page.locator("//a[@href='/category_products/1']")
    women_dress.click()

    category_title = homepage.page.locator("//h2[@class='title text-center']")
    expect(category_title).to_have_text("Women - Dress Products")
    
    men = homepage.page.locator("a[href='#Men']")
    men.click()
    men_tshirts = homepage.page.locator("//a[contains(text(),'Tshirts')]")
    men_tshirts.click()

    expect(category_title).to_have_text("Men - Tshirts Products")

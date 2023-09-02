from playwright.sync_api import Page, expect
from models.login_page import LoginPage

existing_values = {
    "username": "Kamil",
    "email": "dziobzi2137@gmail.com"
}

def test_register_existing_user(page: Page):
    login_page = LoginPage(page)
    login_page.register(**existing_values)
    email_exists = login_page.page.locator("//p[@style='color: red;']")
    expect(email_exists).to_be_visible()
    print("Test 5 completed successfully")
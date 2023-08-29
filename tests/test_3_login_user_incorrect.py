from playwright.sync_api import sync_playwright, Page, expect
import pytest
from models.login_page import LoginPage

incorrect_values = {
    "email": "dziob@gmail.com",
    "password": "987654321"
}

def test_login_incorrect(page: Page):
    login_page = LoginPage(page)
    login_page.login(**incorrect_values)
    expect(login_page.page.locator("//p[@style='color: red;']")).to_be_visible()
    print("Test 3 completed successfully")
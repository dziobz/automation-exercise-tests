from playwright.sync_api import Page
from models.login_page import LoginPage

correct_values = {
    "email": "dziobzi2137@gmail.com",
    "password": "123456789"
}

def test_login_correct(page: Page):
    
    login_page = LoginPage(page)
    
    login_page.login(**correct_values)
    login_page.verify()
    # without deleting account
    print("Test 2 completed successfully")
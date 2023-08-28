from playwright.sync_api import sync_playwright, Page, expect
import pytest
from models.login_page import LoginPage



def test_login_correct(page: Page):
    email = "dziobzi2137@gmail.com"
    password = "123456789"
    
    login_page = LoginPage(page)
    login_page.login_button.click()
    login_page.login(email, password)
    login_page.verify()
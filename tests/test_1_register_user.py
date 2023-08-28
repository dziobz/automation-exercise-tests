from playwright.sync_api import sync_playwright, Page, expect
import pytest
from models.login_page import LoginPage

register_data = {
    'title': "Mr",
    'password': '123456789',
    'date': {
        'day': "18",
        'month': 'May',
        'year': "1996"
    },
    'firstName': 'Kam',
    'lastName': 'Kul',
    'company': 'Kamkul',
    'address': 'Nice street 21',
    'country': 'United States',
    'state': 'Alabama',
    'city': 'Goodcity',
    'zipcode': '2137',
    'number': '21376969'

}

def test_register(page: Page):

    login_page = LoginPage(page)
    login_page.login_button.click()

    name = 'Kamil'
    email = "dziobzi2137@gmail.com"
    login_page.register(name, email)
    login_page.register_form(**register_data)
    login_page.verify()
    # login_page.delete_account()
    print("Test 1 completed successfully")
    
    
from playwright.sync_api import Page, expect
from models.products import ProductPage
import json


def test_download_invoice_after_purchase(page: Page):

    homepage = ProductPage(page)
    homepage.add_to_cart(2)
    homepage.go_to_cart()
    homepage.go_to_checkout()
    try:
        homepage.register("Kamil", "dziobzi2137@gmail.com")
        expect(homepage.page.locator("//p[@style='color: red;']")).not_to_be_visible()
    except:
        print("User already registered")
        homepage.login("dziobzi2137@gmail.com", "123456789")
        homepage.delete_account()
        homepage.page.locator("//a[contains(text(),'Signup / Login')]").click()
        homepage.register("Kamil", "dziobzi2137@gmail.com")
    with open("data.json") as json_file:
        register_data = json.load(json_file)
        homepage.register_form(**register_data)
        homepage.verify()
        homepage.go_to_cart()
        homepage.go_to_checkout()
        homepage.review_order(register_data['title'],
                                register_data['firstName'],
                                register_data['lastName'],
                                register_data['company'],
                                register_data['address'],
                                register_data['country'],
                                register_data['state'],
                                register_data['city'],
                                register_data['zipcode'],
                                register_data['number']),
    with open("card_details.json") as json_file:
        payment_data = json.load(json_file)
        homepage.payment(**payment_data)
    homepage.download_invoice()
    homepage.page.locator("//a[contains(text(), 'Continue')]").click()
    homepage.delete_account()




from playwright.sync_api import Page, expect
from models.homepage import Homepage
import json



def test_place_order_register_while_checkout(page: Page):

    
    homepage = Homepage(page)
    homepage.add_to_cart(1)
    homepage.go_to_cart()
    homepage.go_to_checkout()
    homepage.register("Kamil", "dziobzi2137@gmail.com")
    with open('data.json') as json_file:
        register_data = json.load(json_file)

        homepage.register_form(**register_data)
        homepage.go_to_cart()
        homepage.go_to_checkout()
        
        homepage.review_order(title=register_data["title"],
                              firstName=register_data["firstName"],
                              lastName=register_data["lastName"],
                              company=register_data["company"],
                              address=register_data["address"],
                              country=register_data["country"],
                              state=register_data["state"],
                              city=register_data["city"],
                              zipcode=register_data["zipcode"],
                              number=register_data["number"])
    
    with open("card_details.json") as json_file:
        card_data = json.load(json_file)
        homepage.payment(**card_data)
    homepage.delete_account()
        

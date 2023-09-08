from playwright.sync_api import Page, expect
import requests
from models.login_page import LoginPage

BLOCK_RESOURCE_NAMES = [
  'adzerk',
  'analytics',
  'cdn.api.twitter',
  'doubleclick',
  'exelator',
  'facebook',
  'google',
  'google-analytics',
  'googletagmanager',
]
        ### Blocks ads 
def intercept_route(route):
    if any(key in route.request.url for key in BLOCK_RESOURCE_NAMES):
        return route.abort()
    return route.continue_()


class Homepage(LoginPage):

    def __init__(self, page: Page):
        self.page = page
        self.page.set_viewport_size({"width": 1600, "height": 1200})
        self.page.route("**/*", intercept_route )

        while True:
            try:
                self.page.goto("https://www.automationexercise.com")
            except:
                self.page.wait_for_timeout(5000)
                continue
            break
        expect(self.page).to_have_url("https://www.automationexercise.com/")

    # Choose what item to add to cart
    def add_to_cart(self, number):
        self.product_card = self.page.locator("div.single-products").nth(number-1)
        self.product_card.hover()
        self.product_card.locator("div.overlay-content").locator("a.btn.btn-default.add-to-cart").click()

        self.continue_btn = self.page.locator("button.btn.btn-success.close-modal")
        self.continue_btn.click()

    def add_to_cart_recommended(self):
        self.recommended_heading = self.page.locator("//h2[contains(text(),'recommended items')]")
        self.recommended_heading.scroll_into_view_if_needed()
        self.carousel = self.page.locator("div#recommended-item-carousel")
        self.recommended_item = self.carousel.locator("div.single-products").nth(0)
        self.recommended_item.locator("//a[contains(text(), 'Add to cart')]").click()
        view_cart = self.page.locator("//u[contains(text(),'View Cart')]")
        view_cart.click()
        expect(self.page.locator("//a[contains(text(),'Blue Top')]")).to_be_visible()
    # Remove each item from cart
    def remove_from_cart(self):
        expect(self.page).to_have_url("https://www.automationexercise.com/view_cart")
        self.products = self.page.get_by_role("rowgroup")
        
        for i in range(self.products.count()):
            self.product = self.products.locator(f"tr#product-{i+1}")
            self.product.locator("a.cart_quantity_delete").click()
            expect(self.product).not_to_be_visible()

    # Go to cart
    def go_to_cart(self):
        self.cart = self.page.locator("//a[contains(text(), 'Cart')]")
        self.cart.click()
        expect(self.page).to_have_url("https://www.automationexercise.com/view_cart")

    # Go to checkout
    def go_to_checkout(self):
        expect(self.page).to_have_url("https://www.automationexercise.com/view_cart")
        self.checkout_btn = self.page.locator("a.btn.btn-default.check_out")
        self.checkout_btn.click()
        try:
            self.view_cart = self.page.locator("//u[contains(text(), 'Register / Login')]")
            self.view_cart.click()
        except: 
            "User already logged in"

    # Verify address information
    def review_order(self, title, firstName, lastName, company, address, 
                      country, state, city, zipcode, number):
        expect(self.page.locator("//ul[@id='address_delivery']//li[@class='address_firstname address_lastname'][contains(text(),'Mr. Kam Kul')]")).to_have_text(f"{title}. {firstName} {lastName}")
        expect(self.page.locator("//ul[@id='address_delivery']//li[@class='address_address1 address_address2'][contains(text(),'Kamkul')]")).to_have_text(company)
        expect(self.page.locator("//ul[@id='address_delivery']//li[@class='address_address1 address_address2'][contains(text(),'Nice street 21')]")).to_have_text(address)
        expect(self.page.locator("li.address_city.address_state_name.address_postcode").nth(0)).to_have_text(f"{city} {state} {zipcode}")
        expect(self.page.locator("//ul[@id='address_delivery']//li[@class='address_country_name'][contains(text(),'United States')]")).to_have_text(country)
        expect(self.page.locator("//ul[@id='address_delivery']//li[@class='address_phone'][contains(text(),'21376969')]")).to_have_text(number)
        # Leave a comment
        self.comment = self.page.locator("textarea.form-control")
        self.comment.fill("This is a very nice order")
        # Place an order
        self.page.locator("//a[@class='btn btn-default check_out']").click()

    # Enter card information
    def payment(self, name, cardNumber, cvc, month, year):
        expect(self.page).to_have_url('https://www.automationexercise.com/payment')

        self.name_on_card = self.page.locator("input[name=\"name_on_card\"]")
        self.name_on_card.fill(name)
        self.card_number = self.page.locator("input[name=\"card_number\"]")
        self.card_number.fill(cardNumber)
        self.cvc = self.page.get_by_placeholder("ex. 311")
        self.cvc.fill(cvc)
        self.expiry_month = self.page.get_by_placeholder("MM")
        self.expiry_month.fill(month)
        self.expiry_year = self.page.get_by_placeholder("YYYY")
        self.expiry_year.fill(year)

        pay_btn = self.page.get_by_role("button", name="Pay and Confirm Order")
        pay_btn.click()

        expect(self.page.locator("//b[contains(text(),'Order Placed!')]")).to_be_visible()

    def download_invoice(self):
        # Start waiting for the download
        with self.page.expect_download() as download_info:
            # Perform the action that initiates download
            download_btn = self.page.locator("//a[contains(text(), 'Download Invoice')]")
            download_btn.click() 
        # Wait for the download to start
        download = download_info.value
        # Wait for the download process to complete
        print(download.path())
        # Save downloaded file somewhere
        download.save_as("invoice.txt")
        
               


        

from playwright.sync_api import Page, expect
import requests

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

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.set_viewport_size({"width": 1600, "height": 1200})

        self.page.route("**/*", intercept_route )
        self.page.goto("https://www.automationexercise.com")
        expect(self.page).to_have_url("https://www.automationexercise.com/")
        self.login_button = self.page.locator("//a[contains(text(),'Signup / Login')]")

        self.page.wait_for_load_state()



    def register(self, username, email):
        self.new_user_signup = self.page.get_by_role("heading", name="New User Signup!")

        self.register_name = self.page.get_by_placeholder("Name")
        self.register_email = self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.signup_button = self.page.get_by_role("button", name="Signup")

        expect(self.new_user_signup).to_be_visible()

        self.register_name.fill(username)
        self.register_email.fill(email)
        self.signup_button.click()

    
    def register_form(self, title, password, date, firstName, lastName, company, address, 
                      country, state, city, zipcode, number):
        
        ##### ACCOUNT INFORMATION #####
        self.enter_info = self.page.get_by_role("heading", name="Enter Account Information")
        
        mr_radio = self.page.locator("input#id_gender1")
        mrs_radio = self.page.locator("input#id_gender2")
        if title == "Mr":
            mr_radio.check()
        else:
            mrs_radio.check()
        
        self.password = self.page.get_by_label("Password")
        self.password.fill(password)

        
        self.page.select_option('select#days', label=date["day"])
        self.page.select_option('select#months', label=date["month"])
        self.page.select_option('select#years', label=date["year"])

        self.newsletter = self.page.get_by_role("checkbox", name="newsletter")
        self.newsletter.check()
        self.optin = self.page.locator('input#optin')
        self.optin.check()

        # ADDRESS INFORMATION

        self.firstName = self.page.get_by_label("First name")
        self.firstName.fill(firstName)
        self.lastName = self.page.get_by_label("Last name")
        self.lastName.fill(lastName)
        self.company = self.page.locator("input#company")
        self.company.fill(company)
        self.address = self.page.locator("input#address1")
        self.address.fill(address)
        self.page.select_option('select#country', label=country)
        self.state = self.page.get_by_label("State")
        self.state.fill(state)
        self.city = self.page.get_by_label("City")
        self.city.fill(city)
        self.zipcode = self.page.locator('input#zipcode')
        self.zipcode.fill(zipcode)
        self.number = self.page.get_by_label("Mobile Number")
        self.number.fill(number)
        self.page.screenshot(path="register.jpg", full_page=True)

        self.create_account_btn = self.page.get_by_role('button', name="Create Account")
        self.create_account_btn.click()

        expect(self.page.get_by_role("heading", name="Account Created!")).to_be_visible()
        self.page.locator("//a[@class='btn btn-primary']").click()

        self.logged_in = self.page.locator("//a[contains(text(), 'Logged in as')]")
        expect(self.logged_in).to_have_text("Logged in as Kamil")
        
        self.page.locator('//a[contains(text(), "Delete Account")]').click()
        self.page.locator("//a[@class='btn btn-primary']").click()

    def login(self, email, password):

        self.login_email = self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.login_password = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")



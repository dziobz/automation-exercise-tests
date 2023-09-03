from playwright.sync_api import Page, expect
from models.homepage import Homepage

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

class ProductPage(Homepage):

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


    def products(self):
        self.products_btn = self.page.locator("//a[contains(text(), 'Products')]")
        self.products_btn.click()
        expect(self.page).to_have_url("https://www.automationexercise.com/products")
        expect(self.page.get_by_role("heading", name="All Products")).to_be_visible()
        expect(self.page.locator("div.row").nth(1)).to_be_visible()


    def search_product(self, product):
        expect(self.page).to_have_url("https://www.automationexercise.com/products")
        self.input = self.page.get_by_placeholder("Search Product")
        self.input.fill(product)
        self.search_btn = self.page.locator("button#submit_search")
        self.search_btn.click()
        expect(self.page.get_by_role("heading", name="Searched Products")).to_be_visible()
        self.count = self.page.locator("div.col-sm-4")
        
        for i in range(self.count.count()):
            expect(self.count.nth(i)).to_be_visible()

    
    def verify_brands(self, brand_name):
        if self.page.url != f"https://www.automationexercise.com/brand_products/{brand_name}":
            self.page.locator("//ul[@class='nav navbar-nav']//li//a[contains(text(),'Products')]").click()
        
        expect(self.page.locator("div.brands_products")).to_be_visible()
        brand = self.page.locator(f"//a[text()='{brand_name}']")
        brand.click()
        expect(self.page).to_have_url(f"https://www.automationexercise.com/brand_products/{brand_name}")
        category_title = self.page.locator("//h2[@class='title text-center']")
        expect(category_title).to_contain_text(brand_name)


    def write_review(self, item_number):
        expect(self.page).to_have_url("https://www.automationexercise.com/products")
        view_product = self.page.locator(f"//a[@href='/product_details/{item_number}']")
        view_product.click()

        expect(self.page.locator("//a[contains(text(),'Write Your Review')]")).to_be_visible()
        name = self.page.get_by_placeholder("Name")
        name.fill("Kamil")
        email = self.page.get_by_placeholder("Email Address").nth(0)
        email.fill("dziobzi2137@gmail.com")
        review = self.page.get_by_placeholder("Add Review Here!")
        review.fill("This is a very nice product.")
        submit_btn = self.page.get_by_role("button", name="Submit")
        submit_btn.click()
        
        message = self.page.locator("span", has_text="Thank you for your review.")
        expect(message).to_be_visible()


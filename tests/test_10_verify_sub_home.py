from playwright.sync_api import Page, expect


def test_verify_subscription_homepage(page: Page):
    
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto('https://www.automationexercise.com/', timeout=0)
    expect(page).to_have_url("https://www.automationexercise.com/")
    sub = page.get_by_role("heading", name="Subscription")
    sub.scroll_into_view_if_needed()
    input = page.locator('input#susbscribe_email')
    input.fill("dziobzi@gmail.com")
    sub_btn = page.locator('button#subscribe')
    sub_btn.click()
    expect(page.locator("div.alert-success.alert")).to_be_visible()
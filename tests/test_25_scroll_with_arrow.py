from playwright.sync_api import Page, expect
from models.homepage import Homepage

def test_verify_scroll_up_with_arrow(page: Page):
    
    homepage = Homepage(page)
    subs = homepage.page.locator("//h2[contains(text(),'Subscription')]")
    subs.scroll_into_view_if_needed()
    expect(subs).to_be_in_viewport()
    arrow = homepage.page.locator("a#scrollUp")
    arrow.click()
    heading = homepage.page.get_by_role("heading", name='Full-Fledged practice website for Automation Engineers')
    expect(heading).to_be_visible()
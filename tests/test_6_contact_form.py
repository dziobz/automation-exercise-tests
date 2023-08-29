from playwright.sync_api import sync_playwright, Page, expect
import pytest


def test_contact_form(page: Page):

    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_url("https://www.automationexercise.com/")
    page.locator("//a[contains(text(), 'Contact us')]").click()
    expect(page.get_by_role('heading', name="Get In Touch")).to_be_visible()
    
    name = page.get_by_placeholder("Name")
    name.fill("Kamil")

    email = page.locator("input.form-control").nth(1)
    email.fill("dziobzi2137@gmail.com")

    subject = page.get_by_placeholder("Subject")
    subject.fill("Testing")

    with page.expect_file_chooser() as fc_info:
        page.locator("input.form-control").nth(3).click()
        file_chooser = fc_info.value
        file_chooser.set_files("register.jpg")

    page.locator("input.btn.btn-primary").click()
    page.on("dialog", lambda dialog: print(dialog.message))
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("input.btn.btn-primary").click()
    
    expect(page.locator("div.status.alert.alert-success")).to_be_visible()
    home_btn = page.locator("a.btn.btn-success")
    home_btn.click()
    expect(page).to_have_url("https://www.automationexercise.com/")
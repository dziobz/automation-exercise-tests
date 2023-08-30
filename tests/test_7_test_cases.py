from playwright.sync_api import sync_playwright, Page, expect
import pytest

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
def intercept_route(route):
    if any(key in route.request.url for key in BLOCK_RESOURCE_NAMES):
        return route.abort()
    return route.continue_()


def test_test_cases_page(page: Page):
    page.route("**/*", intercept_route )
    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_url("https://www.automationexercise.com/")
    test_cases = page.locator("//a[contains(text(), 'Test Cases')]")
    test_cases.click()
    expect(page).to_have_url("https://www.automationexercise.com/test_cases")
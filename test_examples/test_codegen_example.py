import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("whatever")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("All is mine!")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_text("whatever").click(button="right")
    page.get_by_text("whatever").click()
    page.get_by_role("listitem").filter(has_text="whatever").get_by_label("Toggle Todo").uncheck()
    page.get_by_role("link", name="All").click()
    page.get_by_role("listitem").filter(has_text="whatever").get_by_label("Toggle Todo").check()
    page.get_by_role("listitem").filter(has_text="All is mine!").get_by_label("Toggle Todo").check()
    page.get_by_text("whatever").click()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_text("Mark all as complete").click()
    page.get_by_role("link", name="real TodoMVC app.").click()
    page.get_by_text("select", exact=True).click()
    page.get_by_role("link", name="View on GitHub").click()
    expect(page.get_by_test_id("anchor-button")).to_match_aria_snapshot("- text: master")
    expect(page.locator("#folder-row-1")).to_match_aria_snapshot("- link \"cypress, (Directory)\"")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

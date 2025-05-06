import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    firefox = playwright.firefox
    browser = firefox.launch()
    context = browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    page = context.new_page()
    page.goto("https://docs.google.com/forms/d/14ZGEMIX5b9PYaRDTS_grx9GEzTNUWfusnXu3_LS1_Xw/viewform?edit_requested=true")
    page.get_by_role("radio", name="Yes, I'll be there").click()
    page.get_by_role("textbox", name="What are the names of people").click()
    page.get_by_role("textbox", name="What are the names of people").fill("asdfadf")
    page.get_by_role("radio", name="Website").click()
    page.get_by_role("list", name="Checkbox Test Pertanyaan wajib", exact=True).get_by_label("Option 1").click()
    page.get_by_role("list", name="Second Checkbox Test").get_by_label("Option 1").click()
    page.get_by_role("radio", name="1", exact=True).click()
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

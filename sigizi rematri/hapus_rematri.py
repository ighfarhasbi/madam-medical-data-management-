import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/")
    page.get_by_role("textbox", name="Tampilkan Password ").click()
    page.get_by_role("textbox", name="Tampilkan Password ").fill("sukaasih")
    page.get_by_role("textbox", name="Masukan kata yang terlihat").click()
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("kereta")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Rematri ").click()
    page.get_by_role("link", name="Daftar Rematri by Domisili").click()
    page.get_by_role("button", name=" Cari Data").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("row", name="2. 3205385112110003 ALIFAH").get_by_role("link").nth(1).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

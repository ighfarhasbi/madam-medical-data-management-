import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/")
    page.get_by_role("textbox", name="").fill("name_here")
    page.get_by_role("textbox", name="").press("Tab")
    page.get_by_role("textbox", name="Tampilkan Password ").fill("pass_here")
    page.get_by_role("textbox", name="Tampilkan Password ").press("Tab")
    page.get_by_role("checkbox").press("Tab")
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("gawai")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Ibu Hamil ").click()
    page.get_by_role("link", name="Daftar Ibu Hamil", exact=True).click()
    page.get_by_role("button", name=" Cari Data").click()
    page.locator("a:nth-child(5)").first.click()
    page.locator("#tgl").click()
    page.get_by_role("cell", name="7").nth(1).click()
    page.locator("#penyebab").click()
    page.locator("#penyebab").fill("sakit ginjal")
    page.locator("#lokasi").click()
    page.locator("#lokasi").fill("singaparna")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

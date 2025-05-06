import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/")
    page.get_by_role("textbox", name="").fill("dssukaasih")
    page.get_by_role("textbox", name="").press("Tab")
    page.get_by_role("textbox", name="Tampilkan Password ").fill("sukaasih")
    page.get_by_role("textbox", name="Masukan kata yang terlihat").click()
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("komputer")
    page.get_by_role("button", name=" Login").click()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/index.php/index.html")
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Balita ").click()
    page.get_by_role("link", name="Daftar Balita", exact=True).click()
    page.goto("https://sigizikesga.kemkes.go.id/ppgbm/index.php/Balita/daftar.html")
    page.locator("a:nth-child(8)").first.click()
    page.get_by_role("link", name="+ Tambah Imunisasi").click()
    page.locator("#tanggal_imunisasi").click()
    page.get_by_role("cell", name="6", exact=True).nth(1).click()
    page.locator("select[name=\"hb\"]").select_option("1")
    page.locator("select[name=\"polio\"]").select_option("2")
    page.locator("select[name=\"campak\"]").select_option("1")
    page.locator("input[name=\"bcg\"]").check()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

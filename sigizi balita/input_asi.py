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
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("kesehatan")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Balita ").click()
    page.get_by_role("link", name="Daftar Balita", exact=True).click()
    page.locator("a:nth-child(7)").first.click()
    page.get_by_role("link", name=" ASI").click()
    page.goto("https://sigizikesga.kemkes.go.id/ppgbm/index.php/balita/asi/3206906507243698.html")
    page.get_by_role("link", name=" Tambah ASI").click()
    page.locator("select[name=\"asi0\"]").select_option("1")
    page.locator("select[name=\"asi1\"]").select_option("0")
    page.locator("select[name=\"asi2\"]").select_option("0")
    page.locator("select[name=\"asi3\"]").select_option("1")
    page.locator("select[name=\"asi4\"]").select_option("0")
    page.locator("select[name=\"asi5\"]").select_option("0")
    page.locator("select[name=\"asi6\"]").select_option("0")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

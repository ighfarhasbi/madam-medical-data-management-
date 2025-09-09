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
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("agenda")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.goto("https://sigizikesga.kemkes.go.id/ppgbm/index.php/index_ppgbm.html")
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Balita ").click()
    page.get_by_role("link", name="Daftar Balita", exact=True).click()
    page.get_by_role("link", name="").nth(1).click()
    page.goto("https://sigizikesga.kemkes.go.id/ppgbm/index.php/Balita/mpasi/3206241904240002.html")
    page.get_by_role("link", name="+ Tambah Pemberian MPASI").click()
    page.get_by_role("textbox").click()
    page.get_by_role("cell", name="6").nth(1).click()
    page.locator("select[name=\"asi\"]").select_option("1")
    page.locator("select[name=\"sereal\"]").select_option("1")
    page.locator("select[name=\"susu\"]").select_option("1")
    page.locator("select[name=\"daging\"]").select_option("1")
    page.locator("select[name=\"telur\"]").select_option("1")
    page.locator("select[name=\"vita\"]").select_option("1")
    page.locator("select[name=\"dapat_intervensi\"]").select_option("1")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

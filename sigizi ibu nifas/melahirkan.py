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
    page.get_by_role("textbox", name="Tampilkan Password ").press("Tab")
    page.get_by_role("checkbox").press("Tab")
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("adopsi")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Ibu Nifas ").click()
    page.get_by_role("link", name="Daftar Ibu Nifas").click()
    page.get_by_role("button", name=" Cari Data").click()
    page.get_by_role("row", name="1. 3206244707850007 ANI").get_by_role("link").nth(2).click()
    page.locator("#tanggal").click()
    page.get_by_role("cell", name="7").nth(1).click()
    page.locator("select[name=\"jk\"]").select_option("2")
    page.locator("select[name=\"tempat\"]").select_option("Poskesdes")
    page.locator("select[name=\"penolong\"]").select_option("Perawat")
    page.locator("textarea[name=\"penyulit\"]").click()
    page.locator("textarea[name=\"penyulit\"]").fill("tidak ada")
    page.get_by_role("form").locator("div").filter(has_text="Penyulit Persalinan").click()
    page.get_by_text("Penolong Persalinan Bidan").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

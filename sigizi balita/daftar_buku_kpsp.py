import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/")
    page.get_by_role("textbox", name="").click()
    page.get_by_role("textbox", name="").fill("name_here")
    page.get_by_role("textbox", name="Tampilkan Password ").click()
    page.get_by_role("textbox", name="Tampilkan Password ").fill("pass_here")
    page.get_by_role("textbox", name="Masukan kata yang terlihat").click()
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("rumah")
    page.get_by_role("button", name=" Login").click()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/index.php/index.html")
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Balita ").click()
    page.get_by_role("link", name="Daftar Balita", exact=True).click()
    page.goto("https://sigizikesga.kemkes.go.id/ppgbm/index.php/Balita/daftar.html")
    page.locator("a:nth-child(6)").first.click()
    page.get_by_role("row", name="1. April 2025 12 April 2025 7").get_by_role("link").click()
    page.get_by_role("row", name="1 Bayi dapat memungut dengan").get_by_label("Ya").check()
    page.get_by_role("row", name="2 Bayi dapat memungut dan").get_by_label("Ya").check()
    page.get_by_role("row", name="3 Bayi mencoba mencari benda").get_by_label("Ya").check()
    page.get_by_role("row", name="4 Bayi mencoba mendapatkan").get_by_label("Tidak").check()
    page.get_by_role("row", name="5 Bayi menengok ke belakang").get_by_label("Ya").check()
    page.get_by_role("row", name="6 Bayi dapat mengatakan 2").get_by_label("Ya").check()
    page.get_by_role("row", name="7 Bayi dapat makan kue kering").get_by_label("Ya").check()
    page.get_by_role("row", name="8 Bayi dapat memindahkan").get_by_label("Ya").check()
    page.get_by_role("row", name="9 Bayi dapat duduk sendiri").get_by_label("Ya").check()
    page.get_by_role("row", name="10 Bayi mencoba berdiri dan").get_by_label("Tidak").check()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

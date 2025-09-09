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
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Balita ").click()
    page.get_by_role("link", name="Daftar Balita", exact=True).click()
    page.locator("a:nth-child(7)").first.click()
    page.get_by_role("link", name="+ Tambah Pengukuran").click()
    page.locator("#TANGGALUKUR").click()
    page.get_by_role("cell", name="6", exact=True).first.click()
    page.get_by_role("textbox", name="Contoh : 8.3").click()
    page.get_by_role("textbox", name="Contoh : 8.3").fill("7.4")
    page.get_by_role("textbox", name="Contoh : 70").click()
    page.get_by_role("textbox", name="Contoh : 70").fill("100.3")
    page.locator("#LILA").click()
    page.locator("#LILA").fill("35")
    page.locator("#UKURLILA").click()
    page.locator("#UKURLILA").fill("25")
    page.locator("select[name=\"UKURBERAT\"]").select_option("1")
    page.locator("#kelas_ibu_balita").select_option("1")
    page.get_by_role("radio", name="Berdiri").check()
    page.get_by_role("radio", name="Ya").check()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

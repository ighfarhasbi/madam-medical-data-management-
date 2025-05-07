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
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("becak")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Anak Prasekolah ").click()
    page.get_by_role("link", name="Daftar Anak Prasekolah").click()
    page.get_by_role("button", name=" Cari Data").click()
    page.locator(".btn-group > a").first.click()
    page.get_by_role("link", name=" Entry Pengukuran").click()
    page.get_by_role("link", name="+ Tambah Pengukuran").click()
    page.locator("#TANGGALUKUR").click()
    page.get_by_role("cell", name="7", exact=True).first.click()
    page.get_by_role("textbox", name="Contoh : 8.3").click()
    page.get_by_role("textbox", name="Contoh : 8.3").fill("30")
    page.get_by_role("textbox", name="Contoh : 70").click()
    page.get_by_role("textbox", name="Contoh : 70").fill("120")
    page.locator("#LILA").click()
    page.locator("#LILA").fill("35")
    page.locator("#UKURLILA").click()
    page.locator("#UKURLILA").fill("25")
    page.locator("select[name=\"UKURBERAT\"]").select_option("1")
    page.locator("#kelas_ibu_balita").select_option("1")
    page.locator("#AddModal").get_by_text("Berdiri").click()
    page.locator("#vita_group").get_by_text("Ya").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

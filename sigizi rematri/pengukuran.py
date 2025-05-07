import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/")
    page.get_by_role("textbox", name="").fill("dssukaasih")
    page.get_by_role("textbox", name="").press("Tab")
    page.get_by_role("textbox", name="Tampilkan Password ").press("Tab")
    page.get_by_role("textbox", name="Tampilkan Password ").click()
    page.get_by_role("textbox", name="Tampilkan Password ").fill("sukaasih")
    page.get_by_role("textbox", name="Tampilkan Password ").press("Tab")
    page.get_by_role("checkbox").press("Tab")
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("gawai")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Rematri ").click()
    page.get_by_role("link", name="Daftar Rematri by Domisili").click()
    page.get_by_role("button", name=" Cari Data").click()
    page.get_by_role("row", name="1. 3206155204070002 AGNIA").get_by_role("link").nth(2).click()
    page.get_by_role("link", name="+ Tambah Pengukuran").click()
    page.locator("#AddModal #TANGGALUKUR").click()
    page.get_by_role("cell", name="7", exact=True).first.click()
    page.get_by_role("textbox", name="Contoh : 12").click()
    page.get_by_role("textbox", name="Contoh : 12").fill("12")
    page.get_by_role("textbox", name="Contoh : 50").click()
    page.get_by_role("textbox", name="Contoh : 50").fill("40")
    page.get_by_role("textbox", name="Contoh : 100").click()
    page.get_by_role("textbox", name="Contoh : 100").fill("111")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

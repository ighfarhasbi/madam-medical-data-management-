import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/")
    page.get_by_role("textbox", name="").fill("name_here")
    page.get_by_role("textbox", name="").press("Tab")
    page.get_by_role("textbox", name="Tampilkan Password ").press("Tab")
    page.get_by_role("textbox", name="Tampilkan Password ").click()
    page.get_by_role("textbox", name="Tampilkan Password ").fill("pass_here")
    page.get_by_role("textbox", name="Tampilkan Password ").press("Tab")
    page.get_by_role("checkbox").press("Tab")
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("rumah")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Anak Prasekolah ").click()
    page.get_by_role("link", name="Daftar Anak Prasekolah").click()
    page.get_by_role("button", name=" Cari Data").click()
    page.locator("a:nth-child(5)").first.click()
    page.get_by_role("row", name="1. Februari 2025 08 Februari").get_by_role("link").click()
    page.get_by_role("row", name="1 Anak dapat menunjuk garis").get_by_label("Ya").check()
    page.get_by_role("row", name="2 Anak dapat menggambar orang").get_by_label("Ya").check()
    page.get_by_role("row", name="3 Anak dapat menyebutkan 2").get_by_label("Ya").check()
    page.get_by_role("row", name="4 Anak dapat menjawab 3").get_by_label("Ya").check()
    page.get_by_role("row", name="5 Anak dapat mengancikan").get_by_label("Ya").check()
    page.get_by_role("row", name="6 Anak dapat ditinggal orang").get_by_label("Ya").check()
    page.get_by_role("row", name="7 Anak dapat sepenuhnya").get_by_label("Tidak").check()
    page.get_by_role("row", name="8 Anak dapat mengenal konsep").get_by_label("Ya").check()
    page.get_by_role("row", name="9 Anak dapat berdiri 1 kaki").get_by_label("Ya").check()
    page.get_by_role("row", name="10 Anak dapat melompat dengan").get_by_label("Ya").check()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

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
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("akuarium")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Anak Prasekolah ").click()
    page.get_by_role("link", name="Daftar Anak Prasekolah").click()
    page.get_by_role("button", name=" Cari Data").click()
    page.locator(".btn-group > a").first.click()
    page.get_by_role("link", name=" Entry Pengukuran").click()
    page.get_by_role("link", name=" Tindakan").click()
    page.locator("#tgl_tindakan").click()
    page.get_by_role("cell", name="7").nth(1).click()
    page.locator("#konseling").select_option("1")
    page.locator("#periksa_kpsp").select_option("1")
    page.locator("#lapor_pkm").select_option("2")
    page.locator("#kunjungan_ulang").select_option("1")
    page.locator("#rujuk_rs").select_option("2")
    page.locator("input[name=\"jkn\"]").nth(1).check()
    page.locator("input[name=\"air\"]").nth(2).check()
    page.locator("input[name=\"jamban\"]").nth(1).check()
    page.get_by_text("Imunisasi BELUM ADA DATA YA").click()
    page.locator("input[name=\"imunisasi\"]").nth(1).check()
    page.locator("input[name=\"rwyt_kehamilan\"]").nth(2).check()
    page.locator("input[name=\"kecacingan\"]").nth(1).check()
    page.locator("input[name=\"merokok\"]").nth(2).check()
    page.get_by_alt_text("Checkbox").check()
    page.get_by_alt_text("Checkbox").uncheck()
    page.get_by_role("textbox", name="Catatan (apabila ada)").click()
    page.get_by_role("textbox", name="Catatan (apabila ada)").fill("catatan sakit")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

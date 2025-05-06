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
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("laptop")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Balita ").click()
    page.get_by_role("link", name="Daftar Balita", exact=True).click()
    page.locator(".even > td:nth-child(14) > a:nth-child(11)").first.click()
    page.locator("#tgl_tindakan").click()
    page.get_by_role("cell", name="6").nth(1).click()
    page.locator("#konseling").select_option("1")
    page.locator("#periksa_kpsp").select_option("2")
    page.locator("#lapor_pkm").select_option("2")
    page.locator("#kunjungan_ulang").select_option("1")
    page.locator("#rujuk_rs").select_option("1")
    page.locator("input[name=\"jkn\"]").nth(1).check()
    page.locator("input[name=\"air\"]").nth(1).check()
    page.locator("input[name=\"jamban\"]").nth(1).check()
    page.locator("input[name=\"imunisasi\"]").nth(1).check()
    page.locator("input[name=\"merokok\"]").first.check()
    page.locator("input[name=\"kecacingan\"]").nth(1).check()
    page.locator("input[name=\"rwyt_kehamilan\"]").nth(1).check()
    page.get_by_alt_text("Checkbox").check()
    page.get_by_role("textbox", name="Penyakit").click()
    page.get_by_role("textbox", name="Penyakit").fill("pusing")
    page.get_by_role("textbox", name="Catatan (apabila ada)").click()
    page.get_by_role("textbox", name="Catatan (apabila ada)").fill("ada pusing saat berjalan")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

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
    page.get_by_role("textbox", name="Masukan kata yang terlihat").fill("kereta")
    page.get_by_role("button", name=" Login").click()
    page.goto("https://sigizikesga.kemkes.go.id/login_sisfo/index.php/index.html")
    page.get_by_role("link", name="Pelayanan Kesehatan").click()
    page.get_by_role("link", name=" ENTRY ").click()
    page.get_by_role("link", name=" Balita ").click()
    page.get_by_role("link", name="Daftar Balita", exact=True).click()
    page.locator("tr:nth-child(8) > td:nth-child(14) > a:nth-child(5)").click()
    page.get_by_role("row", name="3. Maret 2025 08 Maret 2025 5").get_by_role("link").click()
    page.get_by_role("row", name="Bayi bisa mengangkat kepala").locator("label").first.click()
    page.get_by_role("row", name="Bayi bisa menggerakkan kepala").get_by_label("Ya").check()
    page.get_by_role("row", name="Bayi bisa melihat dan menatap").get_by_label("Ya").check()
    page.get_by_role("row", name="Bayi bisa mengoceh spontan").get_by_label("Ya").check()
    page.get_by_role("row", name="Bayi suka tertawa keras? Ya").get_by_label("Tidak").check()
    page.get_by_role("row", name="Bayi bereaksi terkejut").get_by_label("Ya").check()
    page.get_by_role("row", name="Bayi membalas tersenyum").get_by_label("Ya").check()
    page.get_by_role("row", name="Bayi mengenal ibu dengan").locator("label").nth(1).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

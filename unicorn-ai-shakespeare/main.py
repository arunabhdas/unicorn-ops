from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("https://example.com/admin")
    page.goto("https://example.com/admin/auth/login")
    page.get_by_placeholder("e.g. kai@doe.com").click()
    page.get_by_placeholder("e.g. kai@doe.com").fill("jane@doe.com")
    page.get_by_placeholder("e.g. kai@doe.com").press("Tab")
    page.get_by_label("Password*").fill("12345")
    page.get_by_role("checkbox", name="rememberMe").check()
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Content Manager").click()
    page.get_by_role("link", name="Product").click()
    page.get_by_role("link", name="Create new entry").click()
    page.get_by_label("name").click()
    page.get_by_label("name").fill("Floral Dress")
    page.get_by_role("button", name="Click to add an asset or drag and drop one in this area").click()
    page.get_by_role("button", name="Add more assets").click()
    page.get_by_label("Drag & Drop here orBrowse files").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_label("Drag & Drop here orBrowse files").set_input_files("artwork_6_2.png")
    page.get_by_role("button", name="Upload 1 asset to the library").click()
    page.get_by_role("button", name="Finish").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("link", name="Back").click()
    page.get_by_role("gridcell", name="Floral Dress").get_by_text("Floral Dress").click()
    page.get_by_role("button", name="Publish").click()
    page.get_by_role("link", name="Back").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


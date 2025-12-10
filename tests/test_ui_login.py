from framework.login_page import LoginPage
from framework.config import UI_URL

def test_invalid_login(driver):
    driver.get(UI_URL)

    page = LoginPage(driver)
    page.enter_username("wrong")
    page.enter_password("incorrect")
    page.click_login()

    assert "Your username is invalid!" in page.get_error_message()

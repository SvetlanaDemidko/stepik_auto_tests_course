import time
from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_link_button(browser):
    try:
        browser.get(link)
        browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']").click()
    except NoSuchElementException:
        return False
    return True
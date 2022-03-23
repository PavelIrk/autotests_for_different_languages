import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_the_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)   
    result = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert result > 0, "Didn't find items'"

import pytest
from selenium.webdriver.common.by import By


def  test_product_view_sku(browser):
    """
    Test case WERT-1
    """
    browser.get("http://example.com")

URL = "https://testqastudio.me/"

# каждый тест должен начинаться с test_

def test_smoke(browser):
    """
    TC-1: Smoke test
    """

    browser.get(URL)
	# ul [class*="post-11345"]
    element = browser.find_element(by=By.CSS_SELECTOR, value='ul [class*="post-11341"]')
    element.click()

    sku = browser.find_element(by=By.CLASS_NAME, value='sku')
    assert sku.text == 'C0MSSDSUM7', "Unexpected SCU, wait for: C0MSSDSUM7"

def test_top_menu(browser):
    """
    Test case TC-2
    """
    expected_menu = ['Каталог', 'Часто задавамые вопросы', 'Блог', 'О компании', 'Контакты']

    browser.get(URL)
    elements = browser.find_elements(by=By.CSS_SELECTOR, value="[id='primary-menu'] li a")
    result = [el.get_attribute('text') for el in elements]

    assert result ==expected_menu, 'Top menu does not matching to expected'

def test_products_group(browser):
    """
    Test case TC-2
    """
    expected_menu = [
        'Все',
        'Бестселлеры',
        'Горячие товары',
        'Новые товары',
        'Распродажа товаров']
    

    browser.get(URL)
    menu_element = "[class='catalog-toolbar-tabs__content'] a"
    elements = browser.find_elements(by=By.CSS_SELECTOR, value=menu_element)
    assert len(elements) == len(expected_menu), "Unexpected number of products group"
    
     # result=[]
    # for item in expected_menu:
   #  element = browser.find_element(by=By.CSS_SELECTOR, value=item[2])
   # element.click()

    result = [el.get_attribute('text') for el in elements]

    assert result ==expected_menu , 'Top menu does not matching to expected'    
   
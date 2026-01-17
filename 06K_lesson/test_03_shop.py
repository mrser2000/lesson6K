import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()



def test_shop_process(driver):
  
    wait = WebDriverWait(driver, 10)

  
    driver.get("https://www.saucedemo.com/")

    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

   
    backpack_btn = wait.until()
    EC.element_to_be_clickable(
        ((By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Backpack']]//button"))
    )
    backpack_btn.click()

   
    tshirt_btn = wait.until(
        EC.element_to_be_clickable
        ((By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Bolt T-Shirt']]//button"))
    )
    tshirt_btn.click()

    
    onesie_btn = wait.until(
        EC.element_to_be_clickable
        ((By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Onesie']]//button"))
    )
    onesie_btn.click()

   
    cart_link = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_link.click()

    # 5. Нажать Checkout
    checkout_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_btn.click()

   
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    
    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()

   
    total_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text  

    
    expected_total = "$58.29"
    assert f"Total: {expected_total}" == total_text, (
        f"Итоговая сумма не совпадает. Ожидалось: 'Total: {expected_total}', "
        f"получено: '{total_text}'"
    )
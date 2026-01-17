import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()



def test_slow_calculator(driver):
   
 
    wait = WebDriverWait(driver, 55)

   
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

  
    result_element = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    
    
    actual_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert actual_text == "15", (
        f"Неверный результат: ожидалось '15', получено '{actual_text}'"
    )
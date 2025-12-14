import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture(params=['edge', 'safari'])
def driver(request):
   
    if request.param == 'edge':
        driver = webdriver.Edge()
    elif request.param == 'safari':
        
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Неизвестный браузер: {request.param}")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
  
    wait = WebDriverWait(driver, 15)

   
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

  
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")

   
    zip_code_field = driver.find_element(By.NAME, "zip-code")
    zip_code_field.clear()
    zip_code_field.send_keys("")

    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

   
    try:
        zip_code_field = wait.until(
            EC.presence_of_element_located((By.NAME, "zip-code"))
        )
        zip_code_class = zip_code_field.get_attribute("class")
        assert "is-invalid" in zip_code_class, (
            "Поле Zip code должно быть подсвечено красным (класс is-invalid). "
            f"Фактический класс: {zip_code_class}"
        )
    except TimeoutException:
        pytest.fail("Поле Zip code не найдено на странице после отправки формы")

   
    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_name in valid_fields:
        try:
            field = wait.until(
                EC.presence_of_element_located((By.NAME, field_name))
            )
            field_class = field.get_attribute("class")
            assert "is-valid" in field_class, (
                f"Поле {field_name} должно быть подсвечено зелёным (класс is-valid). "
                f"Фактический класс: {field_class}"
            )
        except TimeoutException:
            pytest.fail(f"Поле {field_name} не найдено на странице после отправки формы")
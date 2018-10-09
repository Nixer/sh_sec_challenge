from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FirstPage:

    def __init__(self, driver):
        self.driver = driver
        self.texts = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_all_elements_located((
                By.XPATH, "//div[@class='example']//div[@id='content']//div[normalize-space(text())]")))

    def validate_text_is_present(self):
        for e in self.texts:
            assert e.is_displayed

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import text_check, image_check

class FirstPage:

    def __init__(self, driver):
        self.driver = driver
        self.texts = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_all_elements_located((
                By.XPATH, "//div[@class='example']//div[@id='content']//div[normalize-space(text())]")))
        self.images = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_all_elements_located((
                By.XPATH, "//div[@class='example']//div[@id='content']//img")))

    def validate_long_word_exist(self):
        assert text_check.char_word(self.texts)

    def print_longest_word(self):
        print(text_check.longest_word(self.texts))

    def validate_punisher_image(self):
        assert image_check.punisher(self.images)

    def print_images_names(self):
        assert image_check.images_names(self.images)

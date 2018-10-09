import unittest

from pageobjects.dynamic_content import FirstPage
from values import strings
from webdriver import Driver


class TestDynPage(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_page_texts(self):
        page = FirstPage(self.driver)
        page.validate_long_word_exist()
        page.print_longest_word()

    def test_page_images(self):
        page = FirstPage(self.driver)
        page.print_images_names()
        page.validate_punisher_image()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()

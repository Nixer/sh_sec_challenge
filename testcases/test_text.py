import unittest

from pageobjects.dynamic_content import FirstPage
from values import strings
from webdriver import Driver


class TestWatch(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_page_texts(self):
        page = FirstPage(self.driver)
        page.validate_long_word_exist()
        page.print_longest_word()

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()

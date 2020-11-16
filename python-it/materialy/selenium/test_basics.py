"""
    Test do podstaw selenium
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class TestBasics(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        self.driver.get("http://www.python.org")
        self.assertEqual(self.driver.title, 'Welcome to Python.org')

    def test_element_visible(self):
        self.driver.get("http://www.python.org")
        try:
            self.driver.find_element_by_name("q")
        except NoSuchElementException:
            self.fail("Element not found!")

    def test_pycon_conference_available(self):
        self.driver.get("http://www.python.org")
        elem = self.driver.find_element_by_name("q")
        #print(elem.text)
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        # print(elem.text)
        self.assertIn('Conferences and Workshops', self.driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

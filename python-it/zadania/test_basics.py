"""
    pisanie testow w selenium
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestBasics(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_web_title(self):
        self.assertEqual(self.driver.title,
                         "Welcome to Python.org")

    def test_conference_and_workshops(self):
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        self.assertIn('Conferences and Workshops', self.driver.page_source)

    def tearDown(self):
        self.driver.close()
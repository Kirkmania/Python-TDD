from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # George has started along the Way of the Testing Goat and
        # pretends to check out a new to-do list website
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item pronto
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Play more Call of Duty" into a text box
        inputbox.send_keys('Play more Call of Duty')

        # When he hits enter, the page updates, and now the page lists
        # "1: Play more Call of Duty" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Play more Call of Duty' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a text box inviting him to to add another item.
        # He enters "Make the blog look prettier"
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # George wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him, with some explanatory
        # text to that effect.

        # He visits that URL, his to-do list is still there.

        # Satisfied, he goes back to sleep.

if __name__ == '__main__':
    unittest.main()             # NOTE: tutorial has warnings='ignore' arg, perhaps not needed?
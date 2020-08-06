from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
# import unittest replaced with django.test

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # helper function for testing row text!
    # https://www.obeythetestinggoat.com/book/chapter_post_and_database.html
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # George has started along the Way of the Testing Goat and
        # pretends to check out a new to-do list website
        self.browser.get(self.live_server_url)

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
        # "1: Play more Call of Duty" as an item in a to-do list NOTE: Cool stuff used to be here. f-string and any() function
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Play more Call of Duty')

        # There is still a text box inviting him to to add another item.
        # He enters "Make the blog look prettier"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make the blog look prettier')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('1: Play more Call of Duty')
        self.wait_for_row_in_list_table('2: Make the blog look prettier')

        # George wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him, with some explanatory
        # text to that effect.
        self.fail('Finish the test!')

        # He visits that URL, his to-do list is still there.

        # Satisfied, he goes back to sleep.

# if __name__ == '__main__':      
#     unittest.main()             # NOTE: tutorial has warnings='ignore' arg, perhaps not needed?
                                  # Not needed anymore as using django test runner
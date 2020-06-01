from selenium import webdriver

browser = webdriver.Firefox()

# George has started along the Way of the Testing Goat and
# pretends to check out a new to-do list website
browser.get('http://localhost:8000')

# He notices the page title and header mentions to-do lists
assert 'To-Do' in browser.title, "Browser title was " + browser.title

# He is invited to enter a to-do item pronto

# He types "Play more Call of Duty" into a text box

# When he hits enter, the page updates, and now the page lists
# "1: Play more Call of Duty" as an item in a to-do list

# There is still a text box inviting him to to add another item.
# He enters "Make the blog look prettier"

# The page updates again, and now shows both items on her list

# George wonders whether the site will remember his list. Then he sees
# that the site has generated a unique URL for him, with some explanatory
# text to that effect.

# He visits that URL, his to-do list is still there.

# Satisfied, he goes back to sleep.

browser.quit()
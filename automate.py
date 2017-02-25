# see automation readme file for usage

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

# you need to modify this so it is your subreddit
subreddit = "skeletondev"

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.reddit.com/r/" + subreddit)

# the page is ajaxy so the title is originally this:
print driver.title

# find the element that's name attribute is q (the login box)
inputElement = driver.find_element_by_name("user")

# type in the search
inputElement.send_keys("you need to log in!")

print "giving you 20 seconds to log in"

time.sleep(20)

# TODO Automate the flair stuff

driver.quit()

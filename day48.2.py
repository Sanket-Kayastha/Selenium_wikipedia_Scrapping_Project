from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
#driver.get("https://en.wikipedia.org/wiki/Earthquake")
driver.get("https://www.wikipedia.org/")
#driver.get("https://secure-retreat-92358.herokuapp.com/")

# #Find element by link
# portal = driver.find_element(By.LINK_TEXT, value="Types")
# portal.click()

#Find search input by name
search=driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# name = driver.find_element(By.NAME, value="fname")
# lastname = driver.find_element(By.NAME, value="lname")
# email = driver.find_element(By.NAME, value="email")
# name.send_keys("sanket")
# lastname.send_keys("sri")
# email.send_keys("pky@email.com")

# submit = driver.find_element(By.CSS_SELECTOR, value="form button")
# submit.click()

#driver.quit()

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()


"""------------1------------"""
# driver.get("https://www.amazon.in/")
# sleep(5)

# navbar = driver.find_element(By.ID, "nav-main")

# cat = navbar.find_elements(By.TAG_NAME, "a")

# for i in cat:
#     print(i.text)

# sleep(5)
# driver.quit()


"""------------2------------"""


# driver.get("https://www.imdb.com/chart/top/")
# sleep(5)

# movies = driver.find_elements(By.CLASS_NAME, "ipc-title__text")

# for i in movies[1:11]:
#     print(i.text)

# sleep(5)
# driver.quit()


"""------------3------------"""

# driver.get("https://www.amazon.in/")
# sleep(4)
# a=driver.find_elements(By.TAG_NAME, "img")
# print(len(a))

# sleep(5)
# driver.quit()


"""------------4------------"""
# driver.get("https://demoqa.com/select-menu")
# driver.find_element(By.ID, "withOptGroup").click()
# sleep(2)
# driver.find_element(By.XPATH, "//div[text()='Group 1, option 1']").click()

# sleep(5)
# driver.quit()


"""------------5------------"""
# driver.get("https://www.amazon.in/")
# sleep(4)
# links = driver.find_elements(By.TAG_NAME,"a")
# for link in links:
#     print(link.get_attribute("href"))

# sleep(5)
# driver.quit()

"""------------6------------"""

# driver.get("https://www.google.com")

# search = driver.find_element(By.NAME,"q")
# search.send_keys("laptop")
# sleep(3)

# suggestions = driver.find_elements(By.XPATH,"//li[@role='presentation']")

# for s in suggestions:
#     print(s.text)

# sleep(5)
# driver.quit()

"""------------7------------"""

# driver.get("https://www.amazon.in/")
# sleep(3)

# a = driver.find_element(By.ID, "nav-link-accountList")

# o = ActionChains(driver)
# o.move_to_element(a).perform()
# sleep(2)

# driver.find_element(By.LINK_TEXT, "Your Wish List").click()

# sleep(5)
# driver.quit()

"""------------8------------"""
# driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
# sleep(3)

# driver.switch_to.frame("iframeResult")

# driver.switch_to.frame(0)
# heading = driver.find_element(By.TAG_NAME, "h1").text

# print(heading)

# sleep(5)
# driver.quit()

"""------------9------------"""

# driver.get("https://www.amazon.in/")
# sleep(5)
# a = driver.find_element("id", "twotabsearchtextbox")
# a.send_keys("Laptop")
# a.send_keys(Keys.ENTER)
# sleep(3)
# a = driver.find_elements("xpath", "//h2//span")
# for i in a:
#     print(i.text)
# sleep(5)
# driver.quit()
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from time import sleep
import os

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()


"""-------------------1-------------------"""

# driver.get("https://demowebshop.tricentis.com")

# sleep(2)

# driver.find_element(By.LINK_TEXT, "Books").click()
# driver.find_elements(By.CSS_SELECTOR, ".product-box-add-to-cart-button")[0].click()
# sleep(2)

# driver.find_element(By.LINK_TEXT, "Shopping cart").click()
# sleep(2)
# assert len(driver.find_elements(By.CSS_SELECTOR, ".cart-item-row")) > 0
# print("Product present in cart")
# sleep(2)
# driver.quit()

"""-------------------2-------------------"""

# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# sleep(3)
# driver.find_element(By.LINK_TEXT,"Electronics").click()
# sleep(3)
# driver.find_element(By.XPATH,"//div[@class='sub-category-item']//a[contains(text(),'Cell phones')]").click()
# sleep(2)
# driver.quit()

"""-------------------3-------------------"""
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# sleep(2)

# driver.find_element(By.TAG_NAME, "button").click()
# sleep(5)

# text = driver.find_element(By.ID, "finish").text
# print(text)

# sleep(2)
# driver.quit()

"""-------------------4-------------------"""
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# sleep(2)

# driver.find_element(By.XPATH, "//button[text()='Remove']").click()
# sleep(5)

# driver.find_element(By.XPATH, "//button[text()='Add']").click()
# sleep(2)

# driver.quit()

"""-------------------5-------------------"""

# driver.get("https://demoqa.com/select-menu")
# sleep(2)

# driver.find_element(By.ID, "withOptGroup").click()
# sleep(2)

# driver.find_element(By.XPATH, "//div[text()='Group 2, option 1']").click()
# sleep(2)

# value = driver.find_element(By.ID, "withOptGroup").text
# print(value)

# sleep(2)
# driver.quit()

"""-------------------6-------------------"""
# driver.get("https://demoqa.com/select-menu")
# sleep(2)

# cars = Select(driver.find_element(By.ID, "cars"))

# cars.select_by_visible_text("Volvo")
# cars.select_by_visible_text("Saab")
# cars.select_by_visible_text("Opel")
# sleep(2)

# for i in cars.all_selected_options:
#     print(i.text)

# sleep(2)
# driver.quit()


"""-------------------7-------------------"""
# driver.get("https://demoqa.com/menu/")
# driver.maximize_window()
# sleep(3)
# actions=ActionChains(driver)
# main=driver.find_element(By.XPATH,"//a[text()='Main Item 2']")
# actions.move_to_element(main).perform()
# sleep(2)
# sub=driver.find_element(By.XPATH,"//a[text()='SUB SUB LIST »']")
# actions.move_to_element(sub).perform()
# sleep(2)
# driver.find_element(By.XPATH,"//a[text()='Sub Sub Item 1']").click()
# sleep(2)
# driver.quit()
"""-------------------8-------------------"""
# driver.get("https://demoqa.com/droppable")
# sleep(2)

# source = driver.find_element(By.ID, "draggable")
# target = driver.find_element(By.ID, "droppable")

# a = ActionChains(driver)
# a.drag_and_drop(source, target).perform()
# sleep(2)

# print(target.text)

# sleep(2)
# driver.quit()

"""-------------------9-------------------"""
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# sleep(2)

# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# sleep(2)

# alert = driver.switch_to.alert
# alert.accept()
# sleep(2)

# result = driver.find_element(By.ID, "result").text
# print(result)

# sleep(2)
# driver.quit()

"""-------------------10-------------------"""
# driver.get("https://the-internet.herokuapp.com/upload")
# sleep(2)

# driver.find_element(By.ID, "file-upload").send_keys(r"C:\Users\KIIT\OneDrive\Desktop\capg_python\Selenium\test.txt")
# sleep(2)

# driver.find_element(By.ID, "file-submit").click()
# sleep(2)

# print(driver.find_element(By.ID, "uploaded-files").text)

# sleep(2)
# driver.quit()

"""-------------------11-------------------"""
# driver.get("https://the-internet.herokuapp.com/download")
# sleep(2)

# links = driver.find_elements(By.TAG_NAME, "a")

# for link in links:
#     if link.text != "":
#         file_name = link.text
#         link.click()
#         break

# sleep(5)

# downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# if file_name in os.listdir(downloads_path):
#     print("File downloaded")
# else:
#     print("File not downloaded")

# sleep(2)
# driver.quit()

"""-------------------12-------------------"""
# driver.get("https://demowebshop.tricentis.com")
# sleep(2)

# driver.find_element(By.LINK_TEXT, "Books").click()
# sleep(2)

# buttons = driver.find_elements(By.CSS_SELECTOR, ".product-box-add-to-cart-button")
# buttons[0].click()
# sleep(2)
# buttons[1].click()
# sleep(2)

# driver.find_element(By.LINK_TEXT, "Shopping cart").click()
# sleep(2)

# items = driver.find_elements(By.CSS_SELECTOR, ".cart-item-row")
# print("Total products:", len(items))

# sleep(2)
# driver.quit()

"""-------------------13-------------------"""
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# sleep(3)
# driver.find_element(By.LINK_TEXT,"Books").click()
# sleep(3)
# books=driver.find_elements(By.XPATH,"//div[@class='product-item']")
# for b in books:
#     price=float(b.find_element(By.CLASS_NAME,"price").text.replace("$",""))
#     if price<20:
#         b.find_element(By.XPATH,".//input[@value='Add to cart']").click()
#         sleep(1)
# driver.quit()

"""-------------------14-------------------"""
# import xlrd
# wb = xlrd.open_workbook("test1.xlsx")
# sheet = wb.sheet_by_index(0)
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))

"""-------------------15-------------------"""
#by using attribute
'''driver.find_element(By.XPATH,"//tag[@attribute='value']")'''
#by using text
'''driver.find_element(By.XPATH,"//tag[text()='value']")'''
#by using group indexing
'''driver.find_element(By.XPATH,"(//tag[@attribute='value'])[1]")'''
#by using contains
'''driver.find_element(By.XPATH,"//tag[contains(@attribute,'value')]")'''

'''1. Which locator is generally the fastest in Selenium?
2. Which wait is recommended for handling dynamic elements in Selenium?
3. Which Selenium class is used to handle dropdown listboxes?

Answers->
1. ID
2. Explicit Wait (WebDriverWait) 
3. Select '''
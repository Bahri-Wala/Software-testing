from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\ChromeDriver\chromedriver")
driver.get('http://127.0.0.1:8000/')
time.sleep(1)
element = driver.find_element(by=By.ID, value="search_text")
element.send_keys("phone")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
element = driver.find_elements(by=By.CLASS_NAME, value="link")[0]
link = element.get_attribute("href")
driver.get(link)
time.sleep(2)
element = driver.find_element(by=By.ID, value="add_to_cart")
element.click()
time.sleep(2)
element = driver.find_element(by=By.ID, value="id_login")
element.send_keys("skyh75500@gmail.com")
element = driver.find_element(by=By.ID, value="id_password")
element.send_keys("skyhskyh")
element = driver.find_element(by=By.ID, value="signin")
element.click()
time.sleep(2)
element = driver.find_element(by=By.ID, value="checkout")
link = element.get_attribute("href")
driver.get(link)
time.sleep(2)
element = driver.find_element(by=By.ID, value="same_billing_address_label")
element.click()
time.sleep(1)
element = driver.find_element(by=By.ID, value="use_default_shipping_label")
element.click()
time.sleep(1)
element = driver.find_elements(by=By.ID, value="payment_method")[0]
element.click()
time.sleep(1)
element = driver.find_element(by=By.ID, value="checkout")
element.click()
time.sleep(2)
element = driver.find_element(by=By.ID, value="stripeBtn")
element.click()
time.sleep(2)
element = driver.find_element(by=By.ID, value="logout")
element.click()
time.sleep(2)
element = driver.find_element(by=By.ID, value="signout")
element.click()
time.sleep(2)
driver.quit()

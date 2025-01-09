from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/")
driver.implicitly_wait(3)
driver.maximize_window()
input_element = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//a[@data-test-id='home-hero-sign-in-cta']"))
)
input_element.click()
email_input_element = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='username']"))
)
email_input_element.click()
email_input_element.send_keys("harinivenkat24@gmail.com")
entered_value = email_input_element.get_property("value")
print(f'Entered email is : {entered_value}')

pwd_input_element = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
)
pwd_input_element.click()
pwd_input_element.send_keys("testing")
entered_value = pwd_input_element.get_property("value")
print(f'Entered password is : {pwd_input_element}')

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
signin_button : WebElement = driver.find_element(By.XPATH, "//button[@class='btn__primary--large from__button--floating']")
signin_button.click()

driver.close()

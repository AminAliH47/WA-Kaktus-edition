from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome("C:/Users/amina/Downloads/chromedriver.exe", options=option)

# url = str(input("Please Enter your URL: \n"))
driver.get("https://ui.dev/amiresponsive")
driver.execute_script("window.scrollTo(0, 30)")

search_bar = driver.find_element(By.XPATH, '//*[@id="url"]')

# Turn background to Light
dark_mode_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/button')
dark_mode_btn.click()

sb_url = str(input("Please Enter Your URL you want to get responsive: \n"))

search_bar.send_keys(sb_url)
search_bar.send_keys(Keys.RETURN)


sleep(10)
driver.get_screenshot_as_file("screenshot5.png")
driver.quit()

print("end...")

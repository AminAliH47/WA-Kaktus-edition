from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Config Important Options for Webdriver
option = webdriver.ChromeOptions()
option.add_argument('--headless')


class Analyze:
    webdriver_path = "C:/Users/amina/Downloads/chromedriver.exe"
    saved_path = "C:/Users/amina/OneDrive/Documents/Kaktus"

    def __init__(self, main_url,
                 name, saved_path=saved_path,
                 webdriver_path=webdriver_path):
        self.main_url = main_url
        self.name = name
        self.webdriver_path = webdriver_path
        self.saved_path = saved_path
        self.driver = webdriver.Chrome(self.webdriver_path, options=option)

    def get_whois(self):
        pass

    def get_responsive(self):
        driver = self.driver

        if "https" in self.main_url:
            # Get Responsive website URL
            driver.get("https://ui.dev/amiresponsive")

            # Change window size for image size
            driver.set_window_size(1300, 700)

            # Find searchbar in page
            search_bar = self.driver.find_element(By.XPATH, '//*[@id="url"]')

            # Turn background to Light
            dark_mode_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/button')
            dark_mode_btn.click()

            # Pass Main URL to responsive website
            search_bar.send_keys(self.main_url)
            search_bar.send_keys(Keys.RETURN)

            # Fixing image for good picture by changing style
            sleep(1)
            driver.execute_script("window.scrollTo({top:50, left:0, behavior: 'smooth'})")
            driver.execute_script("document.body.style.zoom='105%'")

            # Save file
            sleep(10)
            driver.save_screenshot(f"{self.saved_path}/responsive.png")
            image = driver.get_screenshot_as_base64()
            print(image)

        elif "http" in self.main_url:
            # Get Responsive website URL
            driver.get("https://ui.dev/amiresponsive")

            # Change window size for image size
            driver.set_window_size(1300, 700)
        return print("Responsive Done!")

    def get_gtmetrix(self):
        pass

    def get_backlinks(self):
        pass

    def get_amp(self):
        pass

    def get_https(self):
        pass

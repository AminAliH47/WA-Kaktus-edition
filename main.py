from selenium import webdriver
from selenium.common import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image
from decouple import config

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
        self.protocol = 'https' if 'https' in main_url else 'http'
        self.saved_path = saved_path
        self.driver = webdriver.Chrome(self.webdriver_path, options=option)

    def _create_directory(self):
        pass

    def _check_exists(self, by, el):
        try:
            self.driver.find_element(by, el)
        except NoSuchElementException:
            return False
        except ElementNotInteractableException:
            return print({'Error': "Element not interactable!", "name": "Checking exists method"})
        return True

    def get_whois(self):
        pass

    def get_responsive(self):
        driver = self.driver

        protocol = self.protocol  # protocol type

        # Hash map to hold reference data
        hash_map = {
            'https_address': "https://ui.dev/amiresponsive",
            'http_address': "https://amiresponsive.co.uk/",
            'https_search': '//*[@id="url"]',
            'http_search': '//input[@name="site"]',
            'https_sleep': 22,
            'http_sleep': 12,
            'https_size': (170, 30, 1230, 700),
            'http_size': (150, 150, 1150, 680),
        }

        # Get Responsive website URL
        driver.get(hash_map[protocol + '_address'])

        # Change window size for image size
        driver.set_window_size(1300, 700)

        # Find searchbar in page
        try:
            search_bar = driver.find_element(By.XPATH, hash_map[protocol + '_search'])
        except NoSuchElementException:
            return print({'Error': 'No such element!', 'Name': 'Responsive'})

        # Pass Main URL to responsive website
        try:
            search_bar.send_keys(self.main_url)
            search_bar.send_keys(Keys.RETURN)
        except ElementNotInteractableException:
            return print({'Error': 'Element not intractable! (Search Field)', 'Name': 'Responsive'})

        if protocol == 'https':
            # Turn background to Light
            dark_mode_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/button')
            dark_mode_btn.click()

        elif protocol == 'http':
            # make page for good picture by removing element
            sleep(1)
            driver.execute_script('document.querySelector([role="main"]).style.background = "#fff"')
            driver.execute_script('document.querySelector(".devices blockquote").remove()')

        # Fixing image for good picture by changing style
        sleep(2)
        driver.execute_script("window.scrollTo({top:70, left:0, behavior: 'smooth'})")
        driver.execute_script("document.body.style.zoom='110%'")

        # Save file
        sleep(hash_map[protocol + '_sleep'])
        driver.save_screenshot(f"{self.saved_path}/responsive.png")

        # Crop and save the image
        image = Image.open(f"{self.saved_path}/responsive.png")
        image.crop(hash_map[protocol + '_size']).save(f"{self.saved_path}/responsive.png")

        return print("Responsive Done!")

    def get_gtmetrix(self):
        driver = self.driver

        # Delete All Cookies
        driver.delete_all_cookies()

        # Get Responsive website URL
        driver.get("https://gtmetrix.com/")

        # Change window size for image size
        driver.set_window_size(1300, 700)

        # === Login Section ===
        sleep(2)
        # Find login page button
        try:
            login_btn = driver.find_element(By.XPATH, '//*[@id="user-nav-login"]/a')
        except NoSuchElementException:
            return print({'Error': 'No such element! (Login Button)', 'Name': 'GTMetrix'})
        login_btn.click()

        # Find email and password field in page
        try:
            email = driver.find_element(By.XPATH, '//input[@name="email"]')
        except NoSuchElementException:
            return print({'Error': 'No such element! (Email Input)', 'Name': 'GTMetrix'})

        try:
            password = driver.find_element(By.XPATH, '//input[@name="password"]')
        except NoSuchElementException:
            return print({'Error': 'No such element! (Password Input)', 'Name': 'GTMetrix'})

        try:
            submit_login_btn = driver.find_element(By.XPATH,
                                                   '//*[@id="menu-site-nav"]/div[2]/div[1]/form/div[4]/button'
                                                   )
        except NoSuchElementException:
            return print({'Error': 'No such element! (Submit Login Button)', 'Name': 'GTMetrix'})

        # /html/body/div[1]/main/article/h1

        # Pass Main URL to responsive website
        email.send_keys(config('EMAIL'))
        password.send_keys(config('PASSWORD'))
        submit_login_btn.click()

        # if self._check_exists(By.XPATH, "/html/body/div[4]/div[1]"):
        #     return print("GTMetrix Login error!")

        sleep(4)
        # Find searchbar in page
        try:
            search_bar = driver.find_element(By.XPATH, '//input[@name="url"]')
        except NoSuchElementException:
            return print({'Error': 'No such element! (Search URL Field)', 'Name': 'GTMetrix'})

        # Pass Main URL to GTMetrix website
        try:
            search_bar.send_keys(self.main_url)
        except ElementNotInteractableException:
            return print({'Error': 'Element Not Interactable (Search URL Field)', 'Name': 'GTMetrix'})

        # Find and submit Main URL to GTMetrix website
        try:
            submit_url_btn = driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/main/article/form/div[1]/div[2]/button'
                                                 )
        except NoSuchElementException:
            return print({'Error': 'No such element! (Submit URL Button)', 'Name': 'GTMetrix'})

        submit_url_btn.click()

        # Fixing image for good picture by changing style
        sleep(59)
        driver.execute_script("window.scrollTo({top:80, left:0, behavior: 'smooth'})")
        driver.execute_script("document.body.style.zoom='90%'")

        # Save file
        driver.save_screenshot(f"{self.saved_path}/gtmetrix.png")

        # Crop and save the image
        image = Image.open(f"{self.saved_path}/gtmetrix.png")
        image.crop((28, 15, 1080, 560)).save(f"{self.saved_path}/gtmetrix.png")

        return print("GTMetrix Done!")

    def get_backlinks(self):
        driver = self.driver

        # Delete All Cookies
        driver.delete_all_cookies()

        # Get Responsive website URL
        driver.get("https://lxrmarketplace.com/seo-inbound-link-checker-tool.html")

        # Change window size for image size
        driver.set_window_size(1300, 700)

        # Find searchbar in page
        try:
            search_bar = driver.find_element(By.XPATH, '//input[@name="url"]')
        except NoSuchElementException:
            return print({'Error': 'No such element! (Search Field)', 'Name': 'Backlinks'})

        # Pass Main URL to backlinks website
        try:
            search_bar.send_keys(self.main_url)
            search_bar.send_keys(Keys.RETURN)
        except ElementNotInteractableException:
            return print({'Error!': 'Element not intractable!'})

        # Fixing image for good picture by changing style
        sleep(1)
        driver.execute_script('document.querySelector("#cookiePopup").remove()')
        driver.execute_script('document.querySelector("#frm-wrap").remove()')

        # Fixing image for good picture by changing style
        driver.execute_script("window.scrollTo({top:30, left:0, behavior: 'smooth'})")

        # Save file
        sleep(3)
        driver.save_screenshot(f"{self.saved_path}/backlinks.png")

        # Crop and save the image
        image = Image.open(f"{self.saved_path}/backlinks.png")
        image.crop((100, 150, 1250, 540)).save(f"{self.saved_path}/backlinks.png")

        return print("Backlinks Done!")

    def get_amp(self):
        pass

    def get_https(self):
        pass

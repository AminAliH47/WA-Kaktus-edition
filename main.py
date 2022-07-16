from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image

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
            'https_sleep': 15,
            'http_sleep': 10,
            'https_size': (170, 30, 1230, 700),
            'http_size': (150, 150, 1150, 680),
        }

        # Get Responsive website URL
        driver.get(hash_map[protocol + '_address'])

        # Change window size for image size
        driver.set_window_size(1300, 700)

        # Find searchbar in page
        search_bar = self.driver.find_element(By.XPATH, hash_map[protocol + '_search'])

        # Pass Main URL to responsive website
        search_bar.send_keys(self.main_url)
        search_bar.send_keys(Keys.RETURN)

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
        sleep(1)
        driver.execute_script("window.scrollTo({top:70, left:0, behavior: 'smooth'})")
        driver.execute_script("document.body.style.zoom='110%'")

        # Save file
        sleep(hash_map[protocol + '_sleep'])
        driver.save_screenshot(f"{self.saved_path}/responsive.png")

        # Crop and save the image
        image = Image.open(f"{self.saved_path}/responsive.png")
        image.crop(hash_map[protocol + '_size']).save(f"{self.saved_path}/responsive.png")

        # if "https" in self.main_url:
        #     # Get Responsive website URL
        #     driver.get("https://ui.dev/amiresponsive")
        #
        #     # Change window size for image size
        #     driver.set_window_size(1300, 700)
        #
        #     # Find searchbar in page
        #     search_bar = self.driver.find_element(By.XPATH, '//*[@id="url"]')
        #
        #     # Pass Main URL to responsive website
        #     search_bar.send_keys(self.main_url)
        #     search_bar.send_keys(Keys.RETURN)
        #
        #     # Turn background to Light
        #     dark_mode_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/button')
        #     dark_mode_btn.click()
        #
        #     # Fixing image for good picture by changing style
        #     sleep(1)
        #     driver.execute_script("window.scrollTo({top:70, left:0, behavior: 'smooth'})")
        #     driver.execute_script("document.body.style.zoom='110%'")
        #
        #     # Save file
        #     sleep(15)
        #     driver.save_screenshot(f"{self.saved_path}/responsive.png")
        #
        #     # Crop and save the image
        #     image = Image.open(f"{self.saved_path}/responsive.png")
        #     image.crop((170, 30, 1230, 700)).save(f"{self.saved_path}/responsive.png")
        #
        # elif "http" in self.main_url:
        #     # Get Responsive website URL
        #     driver.get("https://amiresponsive.co.uk/")
        #
        #     # Change window size for image size
        #     driver.set_window_size(1300, 700)
        #
        #     # Find searchbar in page
        #     search_bar = self.driver.find_element(By.XPATH, '//input[@name="site"]')
        #
        #     # Pass Main URL to responsive website
        #     search_bar.send_keys(self.main_url)
        #     search_bar.send_keys(Keys.RETURN)
        #
        #     # make page for good picture by removing element
        #     sleep(1)
        #     driver.execute_script('document.querySelector([role="main"]).style.background = "#fff"')
        #     driver.execute_script('document.querySelector(".devices blockquote").remove()')
        #
        #     # Fixing image for good picture by changing style
        #     driver.execute_script("window.scrollTo({top:70, left:0, behavior: 'smooth'})")
        #     driver.execute_script("document.body.style.zoom='110%'")
        #
        #     # Save file
        #     sleep(10)
        #     driver.save_screenshot(f"{self.saved_path}/responsive.png")
        #
        #     # Crop and save the image
        #     image = Image.open(f"{self.saved_path}/responsive.png")
        #     image.crop((150, 150, 1150, 680)).save(f"{self.saved_path}/responsive.png")

        return print("Responsive Done!")

    def get_gtmetrix(self):
        pass

    def get_backlinks(self):
        driver = self.driver

        # Get Responsive website URL
        driver.get("https://lxrmarketplace.com/seo-inbound-link-checker-tool.html")

        # Change window size for image size
        driver.set_window_size(1300, 700)

        # Find searchbar in page
        search_bar = self.driver.find_element(By.XPATH, '//input[@name="url"]')

        # Pass Main URL to responsive website
        search_bar.send_keys(self.main_url)
        search_bar.send_keys(Keys.RETURN)

        # Fixing image for good picture by changing style
        sleep(1)
        driver.execute_script('document.querySelector("#cookiePopup").remove()')
        driver.execute_script('document.querySelector("#frm-wrap").remove()')

        # Fixing image for good picture by changing style
        driver.execute_script("window.scrollTo({top:30, left:0, behavior: 'smooth'})")

        # Save file
        sleep(10)
        driver.save_screenshot(f"{self.saved_path}/backlinks.png")

        return print("Backlinks Done!")

    def get_amp(self):
        pass

    def get_https(self):
        pass

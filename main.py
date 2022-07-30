from selenium import webdriver
from selenium.common import (
    ElementNotInteractableException, NoSuchElementException,
    TimeoutException, JavascriptException,
    InvalidArgumentException,
)
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from PIL import (Image, ImageFont, ImageDraw, )
from decouple import config
import requests
import os

# Config Important Options for Webdriver
option = webdriver.ChromeOptions()
option.add_argument("--window-size=1280,1024")

prefs = {"download.default_directory": os.getcwd()}
option.add_experimental_option("prefs", prefs)

option.add_argument('--headless')


class TextColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


txtcolor = TextColors()

class Analyze:
    webdriver_path = "/home/aminali/Downloads/chromedriver"
    saved_path = "/home/aminali/Documents/Kaktus"

    def __init__(self, main_url,
                 name="Analyze", saved_path=saved_path,
                 webdriver_path=webdriver_path):
        self.main_url = main_url
        self.name = name
        self.webdriver_path = webdriver_path
        self.protocol = 'https' if 'https' in main_url else 'http'
        self.saved_path = saved_path
        self.driver = webdriver.Chrome(self.webdriver_path, options=option)

    def create_directory(self):
        """
        Creating a directory with the default name of analysis in the saved path.
        If you enter your desired name, this function will create a directory with the same name for you.

        :return: New saved path
        """
        # Create directory
        path = os.path.join(self.saved_path, self.name)

        try:
            os.mkdir(path)
        except FileExistsError:
            # Save new path in saved path
            self.saved_path = path

            print("Directory already exists!")
            return self.saved_path

        # Save new path in saved path
        self.saved_path = path

        print("Directory Created!")
        return self.saved_path

    def _check_exists(self, by, el):
        """
        Check element exists in page or not.

        :param by: By what basis to find the element?
        :param el: The element you want to find on the page
        :return: If Element exists in page return True, else return False
        """
        try:
            self.driver.find_element(by, el)
        except NoSuchElementException:
            return False
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + '{"Error": "Element not interactable!", "name": "Checking exists method"}')
        return True

    def _wait_until(self, by: str, el: str):
        """
        It checks every five seconds Element Exists in page or not
        If Element Exists in page, It check again else break loop.

        (It's good for when you want check is page reloaded or not)

        :param by: By what basis to find the element?
        :param el: The element you want to find on the page
        """
        driver = self.driver

        while True:
            sleep(5)
            try:
                driver.find_element(by, el)
            except NoSuchElementException:
                break

    def optimize(self):
        import shutil
        import zipfile
        driver = self.driver
        saved_path = self.saved_path

        # Get Image compressor URL
        driver.get("https://imagecompressor.com/")

        # Get Upload Button
        sleep(2)
        try:
            upload_btn = driver.find_element(By.XPATH, '//*[@id="fileSelector"]')
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Upload Button)', 'Name': 'Optimize'}")

        # Upload images
        try:
            upload_btn.send_keys(f"{saved_path}/whois.png")
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (whois image)', 'Name': 'Optimize'}")
        except InvalidArgumentException:
            print(txtcolor.FAIL + "{'Error': 'File not found! (whois image)', 'Name': 'Optimize'}")
            pass

        try:
            upload_btn.send_keys(f"{saved_path}/responsive.png")
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (responsive image)', 'Name': 'Optimize'}")
        except InvalidArgumentException:
            print(txtcolor.FAIL + "{'Error': 'File not found! (responsive image)', 'Name': 'Optimize'}")
            pass

        try:
            upload_btn.send_keys(f"{saved_path}/gtmetrix.png")
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (gtmetrix image)', 'Name': 'Optimize'}")
        except InvalidArgumentException:
            print(txtcolor.FAIL + "{'Error': 'File not found! (gtmetrix image)', 'Name': 'Optimize'}")
            pass

        try:
            upload_btn.send_keys(f"{saved_path}/backlinks.png")
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (backlinks image)', 'Name': 'Optimize'}")
        except InvalidArgumentException:
            print(txtcolor.FAIL + "{'Error': 'File not found! (backlinks image)', 'Name': 'Optimize'}")
            pass

        try:
            upload_btn.send_keys(f"{saved_path}/AMP.png")
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (AMP image)', 'Name': 'Optimize'}")
        except InvalidArgumentException:
            print(txtcolor.FAIL + "{'Error': 'File not found! (AMP image)', 'Name': 'Optimize'}")
            pass

        try:
            upload_btn.send_keys(f"{saved_path}/ssl.png")
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (ssl image)', 'Name': 'Optimize'}")
        except InvalidArgumentException:
            print(txtcolor.FAIL + "{'Error': 'File not found! (ssl image)', 'Name': 'Optimize'}")
            pass

        # Find and click download button
        sleep(2)
        try:
            download_btn = driver.find_element(By.XPATH, '//*[@id="app"]/section[1]/div[3]/button')
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Upload Button)', 'Name': 'Optimize'}")

        sleep(22)
        try:
            download_btn.click()
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (download)', 'Name': 'Optimize'}")

        sleep(12)

        # Remove All unoptimized files
        for file in os.listdir(saved_path):
            try:
                os.remove(os.path.join(saved_path, file))
            except PermissionError:
                return print(txtcolor.FAIL + "{'Error': 'Access is denied (removing file)', 'Name': 'Optimize'}")

        # Move optimized files to saved path directory
        src = os.path.join(os.getcwd(), "imagecompressor.zip")
        dst = os.path.join(saved_path, "imagecompressor.zip")
        try:
            shutil.move(src, dst)
        except FileNotFoundError:
            return print(txtcolor.FAIL + "{'Error': 'File not fount! (move file)', 'Name': 'Optimize'}")

        # Unzip compressed file
        try:
            with zipfile.ZipFile(dst, 'r') as compress:
                compress.extractall(saved_path)
        except FileNotFoundError:
            pass

        return print("Images Optimized!")

    def get_whois(self):
        driver = self.driver
        website_driver = self.driver

        website_driver.get(self.main_url)

        # Get Website title
        title = website_driver.title

        # Get URL from view dns website
        driver.get("https://dnslytics.com/reverse-ip")

        # Find searchbar in page
        try:
            search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/form/input[1]')
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element!', 'Name': 'Whois'}")

        # Import regex
        import re

        # Our whois API
        api_url = "https://www.whoisxmlapi.com/whoisserver/WhoisService"

        # Parameters to send with request
        params = {
            "domainName": self.main_url,
            "apiKey": config("WHOIS_API"),
            "outputFormat": "JSON"
        }

        # Get Response for our website from whois API
        response = requests.request("GET", api_url, params=params).json()
        response = response['WhoisRecord']

        # Archive Required data for whois image
        domain_name = response['domainName']

        # Get register status
        try:
            register_status = response['status']
        except KeyError:
            register_status = "—"

        # Get Nameservers
        try:
            name_servers = "\n".join(response['nameServers']['hostNames'])
        except KeyError:
            name_servers = "—"

        # Dates
        try:
            created_date = f"Created on {response['createdDateNormalized']}"
        except KeyError:
            created_date = "Created on —"
        try:
            updated_date = f"Updated on {response['updatedDateNormalized']}"
        except KeyError:
            updated_date = "Updated on —"
        try:
            expires_date = f"Expires on {response['expiresDateNormalized']}"
        except KeyError:
            expires_date = "Expires on —"

        dates = f'{created_date}\n{expires_date}\n{updated_date}'

        # Pass Main URL to whois website
        sleep(4)
        try:
            search_bar.send_keys(domain_name)
            search_bar.send_keys(Keys.RETURN)
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (Search Field)', 'Name': 'Whois'}")

        # Get IP Address
        sleep(4)
        try:
            raw_dns_text = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[4]/div/div[1]').text
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Raw DNS text)', 'Name': 'Whois'}")
        pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        ip_address = pattern.search(raw_dns_text).group()

        ip_info = requests.get(f"http://ip-api.com/json/{ip_address}").json()

        # Get IP Location
        try:
            ip_city = f" - {ip_info['city']}"
        except KeyError:
            ip_city = ""

        ip_location = ip_info['country'] + ip_city

        # Get country code
        country_code = ip_info['countryCode']

        # Get Hosted website on server
        try:
            hosted_website = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[4]/div/div[1]/b').text
            hosted_website = f" - {hosted_website} other sites hosted on this server"
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Hosted website)', 'Name': 'Whois'}")

        # Get country flag
        flag_url = f'https://countryflagsapi.com/png/{country_code}'
        flag = Image.open(requests.get(flag_url, stream=True).raw)
        flag = flag.convert("RGBA")

        # Resize flag
        (width, height) = (flag.width // 20, flag.height // 20)
        flag = flag.resize((width, height))

        # Load raw whois image
        whois_image = Image.open('assets/images/whois.jpg')

        # Make image editable
        editable = ImageDraw.Draw(whois_image)

        # Load fonts
        font = ImageFont.truetype('assets/fonts/Lato-Regular.ttf', 10)
        domain_font = ImageFont.truetype('assets/fonts/Lato-Regular.ttf', 20)
        title_font = ImageFont.truetype('assets/fonts/Vazirmatn-Regular.ttf', 10)

        # Set colors
        color = (90, 90, 90)
        domain_color = (70, 70, 70)

        # Add text to raw image
        editable.text((165, 0), domain_name, domain_color, font=domain_font)  # Domain name
        editable.text((120, 65), register_status, color, font=font)  # Registrar status
        editable.text((120, 90), name_servers, color, font=font)  # Name servers
        editable.text((120, 159), dates, color, font=font)  # Dates
        editable.text((120, 250), ip_address, color, font=font)  # IP address
        editable.text((195, 250), hosted_website, color, font=font)  # Hosted websites
        editable.text((140, 273), ip_location, color, font=font)  # IP location
        editable.text((120, 330), title, color, font=title_font)  # Website title

        # Add flag to raw image
        whois_image.paste(flag, (120, 275), flag)

        # Save whois image
        whois_image.save(f"{self.saved_path}/whois.png")

        return print("Whois Done!")

    def get_responsive(self):
        driver = self.driver

        # Get Responsive website URL
        driver.get("https://amiresponsive.co.uk/")

        # Change window size for image size
        driver.set_window_size(1280, 1024)

        # Find searchbar in page
        try:
            search_bar = driver.find_element(By.XPATH, '//input[@name="site"]')
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element!', 'Name': 'Responsive'}")

        # Pass Main URL to responsive website
        try:
            search_bar.send_keys(self.main_url)
            search_bar.send_keys(Keys.RETURN)
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable! (Search Field)', 'Name': 'Responsive'}")

        # make page for good picture by removing element
        sleep(2)
        driver.execute_script('document.querySelector([role="main"]).style.background = "#fff"')
        driver.execute_script('document.querySelector(".devices blockquote").remove()')
        try:
            driver.execute_script('document.querySelector("form").remove()')
        except JavascriptException:
            pass

        # Fixing image for good picture by changing style
        sleep(3)
        driver.execute_script("window.scrollTo({top:70, left:0, behavior: 'auto'})")

        # Save file
        sleep(24)
        driver.save_screenshot(f"{self.saved_path}/responsive.png")

        # Crop and save the image
        image = Image.open(f"{self.saved_path}/responsive.png")
        image.crop((140, 90, 1115, 635)).save(f"{self.saved_path}/responsive.png")

        return print("Responsive Done!")

    def get_gtmetrix(self):
        driver = self.driver

        # Delete All Cookies
        driver.delete_all_cookies()

        # Get Responsive website URL
        try:
            driver.get("https://gtmetrix.com/")
            driver.set_page_load_timeout(400)
        except TimeoutException:
            return print(txtcolor.FAIL + "{'Error': 'Page timeout', 'Name': 'GTmetrix'}")

        # Change window size for image size
        driver.set_window_size(1280, 1024)

        # === Login Section ===
        sleep(3)
        # Find login page button
        try:
            login_btn = driver.find_element(By.XPATH, '//*[@id="user-nav-login"]/a')
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Login Button)', 'Name': 'GTMetrix'}")
        login_btn.click()

        # Find email and password field in page
        try:
            email = driver.find_element(By.XPATH, '//input[@name="email"]')
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Email Input)', 'Name': 'GTMetrix'}")

        try:
            password = driver.find_element(By.XPATH, '//input[@name="password"]')
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Password Input)', 'Name': 'GTMetrix'}")

        try:
            submit_login_btn = driver.find_element(By.XPATH,
                                                   '//*[@id="menu-site-nav"]/div[2]/div[1]/form/div[4]/button'
                                                   )
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Submit Login Button)', 'Name': 'GTMetrix'}")

        # Pass Main URL to responsive website
        sleep(3)
        try:
            email.send_keys(config('EMAIL'))
            password.send_keys(config('PASSWORD'))
            submit_login_btn.click()
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element Not Interactable (Email Field)', 'Name': 'GTMetrix'}")

        # Check Email and Password valid for login gtmetrix
        sleep(3)
        if self._check_exists(By.CLASS_NAME, "tooltip-error"):
            return print("GTMetrix Login error!")

        # Find searchbar in page
        sleep(6)
        try:
            search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/main/article/form/div[1]/div[1]/div/input')
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Search URL Field)', 'Name': 'GTMetrix'}")

        # Pass Main URL to GTMetrix website
        sleep(3)
        try:
            search_bar.send_keys(self.main_url)
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element Not Interactable (Search URL Field)', 'Name': 'GTMetrix'}")

        # Find and submit Main URL to GTMetrix website
        sleep(3)
        try:
            submit_url_btn = driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/main/article/form/div[1]/div[2]/button'
                                                 )
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Submit URL Button)', 'Name': 'GTMetrix'}")

        submit_url_btn.click()

        # Wait for analyzing complete
        self._wait_until(By.XPATH, "/html/body/div[1]/main/article/h1")

        # Fixing image for good picture by changing style
        sleep(5)
        driver.execute_script("window.scrollTo({top:80, left:0, behavior: 'auto'})")
        driver.execute_script("document.body.style.zoom='90%'")

        # Save file
        driver.save_screenshot(f"{self.saved_path}/gtmetrix.png")

        # Crop and save the image
        image = Image.open(f"{self.saved_path}/gtmetrix.png")
        image.crop((15, 5, 1070, 600)).save(f"{self.saved_path}/gtmetrix.png")

        return print("GTmetrix Done!")

    def get_backlinks(self):
        driver = self.driver

        # Delete All Cookies
        driver.delete_all_cookies()

        # Get Responsive website URL
        driver.get("https://lxrmarketplace.com/seo-inbound-link-checker-tool.html")

        # Change window size for image size
        driver.set_window_size(1280, 1024)

        # Find searchbar in page
        try:
            search_bar = driver.find_element(By.XPATH, '//input[@name="url"]')
            search_bar.send_keys(self.main_url)
            search_bar.send_keys(Keys.RETURN)
        except NoSuchElementException:
            return print(txtcolor.FAIL + "{'Error': 'No such element! (Search Field)', 'Name': 'Backlinks'}")
        except ElementNotInteractableException:
            return print(txtcolor.FAIL + "{'Error': 'Element not intractable!'}")

        # Pass Main URL to backlinks website
        # try:
        #     search_bar.send_keys(self.main_url)
        #     search_bar.send_keys(Keys.RETURN)
        # except ElementNotInteractableException:
        #     return print(txtcolor.FAIL + "{'Error': 'Element not intractable!'}")

        # Fixing image for good picture by changing style
        sleep(1)
        driver.execute_script('document.querySelector("#cookiePopup").remove()')
        driver.execute_script('document.querySelector("#frm-wrap").remove()')

        # Fixing image for good picture by changing style
        driver.execute_script("window.scrollTo({top:30, left:0, behavior: 'auto'})")

        # Save file
        sleep(3)
        driver.save_screenshot(f"{self.saved_path}/backlinks.png")

        # Crop and save the image
        image = Image.open(f"{self.saved_path}/backlinks.png")
        image.crop((90, 130, 1230, 540)).save(f"{self.saved_path}/backlinks.png")

        return print("Backlinks Done!")

    def get_amp(self):
        # Get URL
        url = self.main_url

        # Load the raw image
        sleep(2)
        raw_amp = Image.open('assets/images/AMP.jpg')

        # Make image editable
        image_editable = ImageDraw.Draw(raw_amp)

        # Load the font
        title_font = ImageFont.truetype('assets/fonts/Roboto-Medium.ttf', 21)

        # Put the URL in image
        image_editable.text((80, 28), url, (255, 255, 255), font=title_font)

        # Save the image
        raw_amp.save(f"{self.saved_path}/AMP.png")

        return print("AMP Done!")

    def get_ssl(self):
        driver = self.driver
        protocol = self.protocol

        # Get URL and SSL
        url = self.main_url

        # Get website URL
        driver.get(url)

        # Load the raw image
        raw_https = Image.open(f'assets/images/{protocol}.jpg')
        raw_https = raw_https.convert("RGBA")

        # Get Favicon
        favicon_url = f'http://www.google.com/s2/favicons?domain={url}'
        favicon = Image.open(requests.get(favicon_url, stream=True).raw)
        favicon = favicon.convert("RGBA")

        # Paste favicon on https raw image
        raw_https.paste(favicon, (17, 8), favicon)

        # Make https raw image editable
        editable = ImageDraw.Draw(raw_https)

        # Add Font to our text
        font = ImageFont.truetype('assets/fonts/Vazirmatn-Regular.ttf', 14)

        # Set coordination for URL
        url_coordination = (172, 42) if protocol == 'https' else (260, 42)

        # Draw URL text in the raw image
        editable.text(url_coordination, url, (255, 255, 255), font=font)

        # Get Title from website
        title = driver.title
        title = (title[:20] + '...') if len(title) > 20 else title
        # Set coordination for Page Title
        title_coordination = (41, 7)
        # Draw Title text in the raw image
        editable.text(title_coordination, title, (255, 255, 255), font=font, direction="ltr")

        # Save the image
        raw_https.save(f"{self.saved_path}/ssl.png", format='png')

        return print("SSL Done!")

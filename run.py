from main import Analyze
import time

url = input("Please Enter Company URL: \n")
name = "شهدین ۲"

SADRA_PATH = ["F:/GitHub/Automation", "F:/GitHub/Automation/chromedriver.exe"]  # Don't touch this line. (NEVER)
AMIN_PATH = ["C:/Users/amina/OneDrive/Documents/Kaktus", "C:/Users/amina/Downloads/chromedriver.exe"]

anz = Analyze(url, name, "F:/GitHub/Automation", "F:/GitHub/Automation/chromedriver.exe")

# Create directory
anz.create_directory()

s = time.time()

# anz.get_whois()
anz.get_responsive()
anz.get_gtmetrix()
anz.get_backlinks()
# anz.get_amp()
# anz.get_ssl()

e = time.time()
print(f'Done in {int(e-s)} seconds.')
# Close Driver After Analyze
anz.driver.close()

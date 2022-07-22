from main import Analyze

url = input("Please Enter Company URL: \n")
name = "مشهد صنعت"

SADRA_PATH = ["F:/GitHub/Automation", "F:/GitHub/Automation/chromedriver.exe"]  # Don't touch this line. (NEVER)

anz = Analyze(url, name)

anz.get_whois()
# anz.get_responsive()
# anz.get_backlinks()
# anz.get_gtmetrix()
# anz.get_amp()
# anz.get_ssl()

# Close Driver After Analyze
anz.driver.close()

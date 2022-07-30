from main import Analyze
import time

# Get Website URL
url = input("Please Enter Website URL: \n")

# Get Website Name
name = input("Please Enter Website Name: (Optional) \n") or "Analyze"
# name = "Analyze" if name == "" else name

# SADRA_PATH = ["F:/GitHub/Automation", "F:/GitHub/Automation/chromedriver.exe"]  # Don't touch this line. (NEVER)
# AMIN_PATH = ["C:/Users/amina/OneDrive/Documents/Kaktus", "C:/Users/amina/Downloads/chromedriver.exe"]

anz = Analyze(url, name)

# Create directory
anz.create_directory()

s = time.time()

anz.get_whois()
anz.get_responsive()
anz.get_gtmetrix()
anz.get_backlinks()
anz.get_amp()
anz.get_ssl()

# Optimize Images
while True:
    optimize = input("\nDo you want to optimize images? (y/n) \n").lower()
    if optimize == "y":
        anz.optimize()
        break
    elif optimize == "n":
        break
    else:
        print("Please enter correct value")

e = time.time()
print(f'Done in {int(e - s)} seconds.')

# Close Driver After Analyze
anz.driver.close()

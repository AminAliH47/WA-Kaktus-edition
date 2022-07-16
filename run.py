from main import Analyze

url = input("Please Enter Company URL: \n")

sadra_paths = ["F:\GitHub\Automation", "F:\GitHub\Automation\chromedriver.exe"]  # Don't touch this line. (NEVER)

anz = Analyze(url, "مشهد صنعت", "F:\GitHub\Automation", "F:\GitHub\Automation\chromedriver.exe")

anz.get_responsive()

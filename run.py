from main import Analyze

url = input("Please Enter Company URL: \n")

anz = Analyze(url, "مشهد صنعت")

# anz.get_responsive()
# anz.get_backlinks()
anz.get_gtmetrix()

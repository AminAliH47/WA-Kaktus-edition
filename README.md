<h1 align="center">
Website Analyzer
</h1>

<div align="center">

*🌵 Kaktus edition 🌵*

Give the program a website URL,
and it will give you 6 analyzes 
including `Whois`, `Responsive`, `GTmetrix`, `Backlinks`, `AMP` and `SSL` test.

</div>
<hr>

Working with project is very simple.
> But it requires a little configuration to run properly.

<br>

# ⚙ Configure the project


First you should make venv for this project.
So in the main root of project you should type this command in your Terminal or Console: 


```
python -m venv venv
```

Now you should activate your venv.
So in the main root of project you should type this command in your Terminal or Console: 

**In Linux/macOS:**

```
source venv/bin/activate
```

**In Windows:**

```
venv/Scripts/activate.ps1
```

After activating venv you should install the **requirements.txt** packages. 
So type this command in your Terminal or Console:

```
pip install -r requirements.txt
```

**⚠ IMPORTANT ⚠**
> If you are using Microsoft Windows OS and want to Analyze RTL (right-to-left) website you need to 
install *Libraqm* Library on your OS.

- [This Link](https://stackoverflow.com/questions/57545244/installing-raqm-libraqm-windows-10) may be useful

### 🔵 Get APIs
> To get **Whois** and **Gtmetrix** analysis, you need to get the 
API of these websites and then save it in the `.env` file.

- Signup to [Whois Website](https://main.whoisxmlapi.com/signup?lang=en) and
get API Key from settings in your panel
- Signup to [GTmetrix Website](https://gtmetrix.com/) and keep the email and password 
you registered with on the website

After getting Whois API and GTmetrix Email and Password 
in the Main root of the project you should create environment variable (`.env`) file.

Your `.env` file should be like this:
```
WHOIS_API=YOUR_WHOIS_API_KEY
EMAIL=YOUR_GTMETRIX_REGISTRED_EMAIL
PASSWORD=YOUR_GTMETRIX_REGISTRED_PASSWORD
```
Then save `.env` file.

### 🔵 Webdriver and Saved path
> You should config **Webdriver** and folder **Saved path** in `main.py` file.
Webdriver and saved path variable are in `__init__` method of `Analyze` class.

[Chrome Webdriver link](https://chromedriver.chromium.org/downloads). You need to download the 
web driver version according to your Chrome browser version.

✅ Project configuration completed successfully. 🎉

<br>

### 🏁 Run and Use Project
After configuring the project correctly, now you need to run the project.

In the Main root of project you should type this command in your Terminal or Console:
```commandline
python run.py
```
After running the program, you must enter the URL address of the website you want to 
analyze and then give the name of the folder (Optional) where you want the analyses to be saved.

✅ Then wait until the analysis is completed. After all 6 analyzes are completed, it will ask you 
if you want to optimize the photos or not, 
if your answer is `y`, it will start optimizing the photos and then save the photos. 

<br>

<h6 align="center"> 
Licensed By Coilaco
</h6>
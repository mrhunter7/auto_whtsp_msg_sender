from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import schedule
import time
import os

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 20)

def send_message():
    try:
        friend_name = os.getenv('FRIEND_NAME', 'FRIEND_NAME')
        message = os.getenv('MESSAGE', 'Günaydın! Bu günlük mesajınız.')
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')))
        search_box.click()
        search_box.send_keys(friend_name + Keys.ENTER)
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"copyable-text selectable-text")][@data-tab="9"]')))
        message_box.send_keys(message + Keys.ENTER)
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        driver.quit()

# Example: Schedule the message to be sent every day at 8 AM
schedule.every().day.at("08:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)

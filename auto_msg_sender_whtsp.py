# WhatsApp Web ve Selenium ile Otomatik Mesaj Gönderme
# Adımlar:
# Gerekli Kütüphaneleri Yükleyin:

# pip install selenium schedule
# WebDriver'ı İndirin:

# ChromeDriver veya GeckoDriver indirin ve bilgisayarınıza kurun.
# Kodunu Yazın:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import schedule
import time

# WhatsApp Web'e giriş yapın ve tarayıcı penceresini açık bırakın
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com")

def send_message():
    try:
        # Arkadaşınızın ismini buraya yazın (tam olarak WhatsApp'taki gibi)
        friend_name = "FRIEND_NAME"
        message = "Günaydın! Bu günlük mesajınız."

        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(friend_name + Keys.ENTER)

        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
        message_box.send_keys(message + Keys.ENTER)

        print("Mesaj gönderildi.")
    except Exception as e:
        print(f"Mesaj gönderilemedi: {e}")

# Zamanlama işlevini kurun
schedule.every().day.at("08:00").do(send_message)  # Her gün saat 08:00'de mesaj gönderir

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()

    
# Açıklamalar
# WhatsApp Web Oturumu:

# Kodu çalıştırdığınızda, WhatsApp Web açılır ve QR kodunu tarayarak oturum açmanız istenir. Oturumu bir kez açtıktan sonra tarayıcı penceresini kapatmayın.
# Kişi Arama ve Mesaj Gönderme:

# Kişi adı friend_name değişkenine, mesaj ise message değişkenine yazılır.
# XPath kullanılarak arama kutusu ve mesaj kutusu bulunur ve mesaj gönderilir.
# Zamanlama:

# schedule kütüphanesi ile her gün belirli bir saatte (08:00) send_message fonksiyonu çalıştırılır.
# Bu yöntem, WhatsApp Web ve Selenium kullanarak belirli bir saatte otomatik olarak mesaj göndermeyi sağlar. Ancak, tarayıcı penceresinin açık kalması ve oturumun sürekli aktif olması gerektiğini unutmayın. 
# Ayrıca, WhatsApp Web'in otomatikleştirilmiş kullanımını tespit etme ve engelleme ihtimali bulunduğunu da göz önünde bulundurun.
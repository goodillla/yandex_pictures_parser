from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, requests, glob, os

driver = webdriver.Chrome()
driver.get('https://yandex.ru/images/search?text=%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%BC%D1%83%D0%B6%D0%B8%D0%BA%D0%BE%D0%B2%20%D1%81%20%D0%B3%D0%BE%D0%BB%D1%8B%D0%BC%20%D1%82%D0%BE%D1%80%D1%81%D0%BE%D0%BC&isize=large')

first_elem = driver.find_element(By.CLASS_NAME, 'serp-item__thumb')
first_elem.click()
time.sleep(1)

# Будем качать с последнего файла
list_of_files = glob.glob('.\pics\*')
try:
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file_number = int(latest_file[7:11])
except:
    latest_file_number = 0

i = 1
for i in range (1,300): #зададим сколько картинок нужно скачать
    btn_view = driver.find_element(By.CLASS_NAME, 'MMViewerButtons-OpenImage')
    href = btn_view.get_attribute('href')
    btn_view.send_keys(Keys.DOWN)
    time.sleep(1)

    print (i)
    if i > latest_file_number:
        file_name = 'pics\%s.jpg' %str(i).zfill(4)
        response = requests.get(href, verify=False)
        time.sleep(3)
        open(file_name, "wb").write(response.content)

driver.quit()
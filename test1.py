from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://ya.ru/"
browser = webdriver.Chrome()
browser.get(link)

search_vxod = browser.find_element(By.XPATH, "/html/body/main/div[2]/div/a[1]")
search_vxod.click()

search_pochta = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button")
search_pochta.click()

search_pochta_vvod = browser.find_element(By.ID, "passp-field-login")
search_pochta_vvod.send_keys("testlogin@yandex.ru")

knopka_voiti = browser.find_element(By.ID, "passp:sign-in")
knopka_voiti.click()

search_password_vvod = browser.find_element(By.ID, "passp-field-passwd")
search_password_vvod.send_keys("testpassword")

knopka_voiti.click()

search_envelope = browser.find_element(By.XPATH, "/html/body/main/div[1]/div/a[1]/div/svg/path")

if search_envelope:
    print('Значок конверта есть. Тест пройден успешно.')
else:
    print('Значка конверта нет. Тест провалился.')

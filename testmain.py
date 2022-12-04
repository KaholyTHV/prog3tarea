from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytest import mark


@mark.parametrize("usuario,passw", [("brucelee", "0777"), ("chavo", "tata"), ("Admin", "admin123"), ("amongu", "0777")])
def testLogin(usuario,passw):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    user = driver.find_element(By.XPATH, '//div/input[@name="username"]')
    contra = driver.find_element(By.XPATH, '//div/input[@name="password"]')
    user.send_keys(usuario)
    contra.send_keys(passw)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    carpeta = "foto" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('foto/login/'+carpeta+'.png')
    time.sleep(3)
    testeo = '01'
    try:
        testeo = driver.find_element(By.XPATH, '//div[@class="oxd-alert-content oxd-alert-content--error"]').text
    except: pass
    assert testeo == '01'

def testPruebaBusqueda():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    user = driver.find_element(By.XPATH, '//div/input[@name="username"]')
    contra = driver.find_element(By.XPATH, '//div/input[@name="password"]')
    user.send_keys("Admin")
    contra.send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@class="oxd-main-menu-search"]/input').send_keys('p')
    data = driver.find_element(By.XPATH, '//div[@class="oxd-sidepanel-body"]//li[1]//span').text
    time.sleep(5)
    carpeta = "foto" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('foto/busqueda/'+carpeta+'.png')
    assert data == "PIM"


def testBtnAdmin():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    user = driver.find_element(By.XPATH, '//div/input[@name="username"]')
    contra = driver.find_element(By.XPATH, '//div/input[@name="password"]')
    user.send_keys("Admin")
    contra.send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li[1]').click()
    carpeta = "foto" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('foto/admin/'+carpeta+'.png')
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'



def testDirectory():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    user = driver.find_element(By.XPATH, '//div/input[@name="username"]')
    contra = driver.find_element(By.XPATH, '//div/input[@name="password"]')
    user.send_keys("Admin")
    contra.send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li[9]').click()
    carpeta = "foto" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('foto/directory/'+carpeta+'.png')
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory'

def testBtnMyInfo():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    user = driver.find_element(By.XPATH, '//div/input[@name="username"]')
    contra = driver.find_element(By.XPATH, '//div/input[@name="password"]')
    user.send_keys("Admin")
    contra.send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li[6]').click()
    carpeta = "foto" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('foto/myinfo/'+carpeta+'.png')
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7'





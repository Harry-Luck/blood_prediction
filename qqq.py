import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import date, datetime

if __name__ == '__main__':
    driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
    driver.get('https://bc.game/crash')
    btn_signin = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div[2]/p'))).click()
    input_email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[1]/div[1]/div[2]/input'))).send_keys('gj19950125@gmail.com')
    input_password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[1]/div[2]/div[2]/input'))).send_keys('qurcjehdrod2022!@#')
    ctime = 0
    ptime = datetime.now()
    flag = 0
    time_flag = 0
    temp_total = 0
    temp_total = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/span'))).text
    while 1:
        try:
            bet_button = driver.find_elements(By.XPATH, '//*[@id="crash-control-0"]/div[2]/div/button/div')
            if bet_button[0].text == 'Bet':
                break
        except:
            bet_button = driver.find_elements(By.XPATH, '//*[@id="crash-control-0"]/div[2]/div/button/div')
            if bet_button[0].text == 'Bet':
                break
    while 1:
        result = 0
        try:
            try:
                bet_button = driver.find_elements(By.XPATH, '//*[@id="crash-control-0"]/div[2]/div/button/div')
            except:
                bet_button = driver.find_elements(By.XPATH, '//*[@id="crash-control-0"]/div[2]/div/button/div')
            bet_button_text = bet_button[0].text
            if bet_button_text == "Bet" and flag == 0:
                if time_flag == 0:
                    ctime = datetime.now()
                    differ = ctime-ptime
                    ptime = ctime
                print(differ.seconds, type(differ.seconds))
                with open("Data.txt", 'a') as fp:
                    fp.write(str(differ.seconds))
                    fp.write('\n')
                flag = 1
            elif bet_button_text != "Bet":
                flag = 0
                continue
        except:
            print("Error")
            continue
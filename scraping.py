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
    
    signin = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/p'))).click()
    input_email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[1]/div[1]/div[2]/input'))).send_keys('michelpoden1021@gmail.com')
    input_password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[1]/div[2]/div[2]/input'))).send_keys('jsy123320')
    btn_signin = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/button[1]/div'))).click()
    
    time.sleep(20)
    temp = 0
    flag = 0
    while(1):  
        try:
            time.sleep(3)    
            try:
                bet_button = driver.find_elements(By.XPATH, '//*[@id="crash-control-0"]/div[2]/div/button/div')
            except:
                bet_button = driver.find_elements(By.XPATH, '//*[@id="crash-control-0"]/div[2]/div/button/div')
            bet_button_text = bet_button[0].text
            if bet_button_text == "Bet":
                group_data = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="game-crash"]/div[2]/div/div[1]/div[1]/div[2]/div'))).text
                split_data = group_data.split()
                # length = len(split_data)
                if temp != split_data[0]:
                    id1 = split_data[0]
                    data = split_data[5]
                    temp = id1
                    with open("Data.txt", 'a') as fp:
                        fp.write(split_data[4])
                        fp.write(':')
                        fp.write(data[:-1])
                        fp.write('\n')
        except:
            print("Error")
            continue
    
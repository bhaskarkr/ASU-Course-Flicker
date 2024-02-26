# from selenium import webdriver
import os
import time
import subprocess
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager
import helper.chrome_helper as youtube_helper




def open_chrome(url):
    # os.system('open -na "Google Chrome" --args -incognito "www.youtube.com"')
    # time.sleep(2)
    # print(url)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.implicitly_wait(0.5)
    # chrome_options = uc.ChromeOptions(use_subprocess=True)
    # chrome_options.add_argument("--incognito")
    # driver = uc.Chrome(options=chrome_options)
    # firefox_profile = uc.FirefoxProfile()
    # firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    # driver = webdriver.Firefox(firefox_profile=firefox_profile)
    c = 0
    # clicked = False
    clicked = True
    os.system('say "Script started"')
    while 1:
        try:
            # os.system('say ""')   
            print("running")
            driver.get(url)
            time.sleep(2)
            data = driver.page_source
            if (not clicked) and c % 50 == 20:
                print("reloading")
                youtube_helper.reload_page()
            
            # print(str(data))


            # if str(data).find("11088") != -1:
            #     print("SPPQM")
            #     if not clicked:
            #         print("clicked")
            #         clicked = True
            #         youtube_helper.click_submit()
            #     os.system('say "s p p q m"')
            #     if str(data).find("90") != -1:
            #         os.system('say "Seats also"')
            # else:
            #     print("not found")

            # # print(str(data))
            # if str(data).find("30326") != -1:
            #     print("SVVT")
            #     os.system('say "s v v t"')
            #     if str(data).find("145") != -1:
            #         os.system('say "Seats also"')
            # else:
            #     print("not found")
            #
            if str(data).find("19657") != -1:
                print("SWM")
                if not clicked:
                    print("clicked")
                    clicked = True
                    youtube_helper.click_submit()
                os.system('say "s w m"')
                if str(data).find("175") != -1:
                    os.system('say "Seats also"')


            # if str(data).find("24342") != -1:
            #     print("IAAS")
            #     os.system('say "security"')
            #     if str(data).find("120") != -1:
            #         os.system('say "Seats also"')
            print(c)
            c += 1
            if c % 5000 == 0:
                os.system('say "Laptop ON"')
        except:
            os.system('say "Error Occured"')
            time.sleep(5)
    os.system('say "Script stopped"')
    # print(data)
    # l = driver.find_element_by_xpath("//a[text()='Privacy Policy']")


    # sign_in_button = driver.find_element(By.XPATH, "/html[1]/body[1]/ytd-app[1]/div[1]/div[1]/ytd-masthead[1]/div[3]/div[3]/div[2]/ytd-button-renderer[1]/yt-button-shape[1]/a[1]/yt-touch-feedback-shape[1]/div[1]/div[2]")
    # sign_in_button.click()
    # enter_email = driver.find_element(By.ID, "identifierId")
    # enter_email.click()
    # enter_email.send_keys("garfielda035")
    # enter_email.send_keys(Keys.RETURN)
    # enter_email.send_keys("garfielda035")
    # pyautogui.hotkey('Command', 'ctrl', 'f')

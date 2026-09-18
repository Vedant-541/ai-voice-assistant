from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

#by the help of chromedriver using Chrome
chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--headless=new")#operating chrome from backend
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

website = r'https://ttsmp3.com/text-to-speech/British%20English/' #website which is to be used
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value='//*[@id="sprachwahl"]'))
ButtonSelection.select_by_visible_text('British English / Brian')  #selecting voice to be used

def Speak(Text):

    lenghtoftext = len(str(Text))

    if lenghtoftext==0:
        pass

    else:
        print("")
        print(f"VOICE ASSISTANT : {Text}")
        print("")
        Data = str(Text)
        xpathofsec = '//*[@id="voicetext"]'   #area where text which has to be read is pasted
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()  #path for read button
        driver.find_element(By.XPATH,value='//*[@id="voicetext"]').clear() #clearing the text area

        if lenghtoftext>=30:
            sleep(4)

        elif lenghtoftext>=40:
            sleep(6)

        elif lenghtoftext>=55:
            sleep(8)

        elif lenghtoftext>=70:
            sleep(10)

        elif lenghtoftext>=100:
            sleep(13)

        elif lenghtoftext>=120:
            sleep(14)

        else:
            sleep(2)

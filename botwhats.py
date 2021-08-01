from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\WorkSpace\Vscode\Projetos\bot-whatsapp\chromedriver.exe")
driver.get('https://web.whatsapp.com')
time.sleep(10)

def bot():
    try: 
        getNewMessages = driver.find_element_by_class_name('_23LrM')
        getNewMessages = driver.find_elements_by_class_name('_23LrM')
        selectionMessages = getNewMessages[-1]
        getMessages = webdriver.common.action_chains.ActionChains(driver)
        getMessages.move_to_element_with_offset(selectionMessages,0,-20)
        getMessages.click()
        getMessages.perform()
        getMessages.click()
        getMessages.perform()

        


    except:
        print('Buscando novas mensagens')
        time.sleep(5)



while True:
    bot()
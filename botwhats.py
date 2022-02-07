from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\WorkSpace\Vscode\Projetos\bot-whatsapp\chromedriver.exe")
driver.get('https://web.whatsapp.com')
time.sleep(10)

def bot():
    try: 
        #PEGA A MENSAGEM DO CLIENTE  
        getNewMessages = driver.find_element_by_class_name('_23LrM')
        getNewMessages = driver.find_elements_by_class_name('_23LrM')
        selectionMessages = getNewMessages[-1]
        getMessages = webdriver.common.action_chains.ActionChains(driver)
        getMessages.move_to_element_with_offset(selectionMessages,0,-20)
        getMessages.click()
        getMessages.perform()
        getMessages.click()
        getMessages.perform()
        #PEGA O NÚMERO DO CLIENTE 
        fone_client = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div/div/div/div/div[2]/div[1]/div[1]/span/span')
        fone_text = fone_client.text
        print(fone_text)
        #nada
        

        


    except:
        print('Buscando novas mensagens')
        time.sleep(5)



while True:
    bot()
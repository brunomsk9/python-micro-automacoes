from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=r'./chromedriver.exe',
                           options=chrome_options)
browser.get('https://google.com/')
browser.find_element_by_xpath("//input[@title='Pesquisar']").send_keys('Especialista RPA')
browser.find_element_by_xpath("//input[@title='Pesquisar']").send_keys(Keys.RETURN)



# Caso queira fechar o Browser tirar o comentário
# browser.quit()



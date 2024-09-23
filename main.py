from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

"""
Função para abrir o navegador

Parâmetros:
- driver: qual navegador vai ser usado
- url: url a ser aberta quando o navegador é aberto
"""   
def open_browser(driver, url):
    driver.get(url)
    driver.maximize_window()

"""
FUnção para preencher os campos do formulário

Parâmetros:
- driver: qual navegador vai ser usado
- xpath_list: lista de xpath's dos campos a serem usados
- sheet: planilha a ser usada
- sheet_columns: colunas da planilha
- url: url do formulário para ser recarregado sempre que for completo
- wait: VALOR OPICIONAL, define o tempo de espera para encontrar cada elemento,
    se não for informado um valor, o padrão será 20
"""
def fill_fields(driver, xpath_list, sheet, sheet_columns, url, wait = 20):
    for i in range(len(xpath_list)):
        for j, xpath in enumerate(xpath_list):
            # verifica onde parar de escrever valores, nesse caso para uma planilha de 6 elementos
            if j < 5:
                driver.find_element(By.XPATH, xpath).send_keys(sheet[sheet_columns[j]][i])
                driver.implicitly_wait(wait)
            else:
                driver.find_element(By.XPATH, xpath).click()
                driver.implicitly_wait(wait)
                
                driver.get(url)
                driver.implicitly_wait(wait)
    
def main():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfnJG4mYhJLO44hFTPyVOBr3Kh2FRkYT4Bo40jB3maxaAIi9g/viewform"
    xpath_list = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea',
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    ]
    
    sheet = pd.read_excel("sheets.xlsx")
    columns = sheet.columns
    
    driver = webdriver.Chrome()
    open_browser(driver, url)
    fill_fields(driver, xpath_list, sheet, columns, url)

if __name__ == "__main__":
    main()
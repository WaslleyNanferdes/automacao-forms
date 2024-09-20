from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

def openBrowser(driver, url):
    driver.get(url)
    driver.maximize_window()
    
def main():
    sheet = pd.read_excel("sheets.xlsx")
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfnJG4mYhJLO44hFTPyVOBr3Kh2FRkYT4Bo40jB3maxaAIi9g/viewform"
    print(sheet.head())
    driver = webdriver.Chrome()
    openBrowser(driver, url)

if __name__ == "__main__":
    main()
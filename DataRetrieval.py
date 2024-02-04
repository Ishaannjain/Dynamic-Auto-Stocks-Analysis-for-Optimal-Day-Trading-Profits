from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from reader import reader
from tabulate import tabulate
import time

options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def getTop():
    driver.get("https://stockanalysis.com/list/car-company-stocks/")
    driver.find_element(By.ID, "change").click()
    r = reader()
    r.feed(driver.page_source)
    data = r.getData()
    processedData = []
    for row in data:
        if len(row) > 0:
            if (row[1] == "Symbol " or row[1] == "CARZ") or row[5] == "-":
                continue
            processedData.append([row[1],row[2],float(row[5][0:len(row[5])-1])])
    return processedData

def getHistoricData(symbol: str):
    driver.get("https://www.nasdaq.com/market-activity/stocks/"+symbol.lower()+"/historical")
    r = reader()
    r.feed(driver.page_source)
    data = r.getData()
    processedData = []
    for row in data:
        if len(row) > 0:
            print(row)
    return processedData

def closeStream():
    driver.quit()

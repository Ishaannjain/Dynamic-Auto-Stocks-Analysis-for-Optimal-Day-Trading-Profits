from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from reader import reader
from tabulate import tabulate
import time

class Driver:
    def __init__(self) -> None:
        self.driver = None
    
    def setUp(self):    
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Firefox(options=options)
        
    def getTop(self):
        self.driver.get("https://stockanalysis.com/list/car-company-stocks/")
        self.driver.find_element(By.ID, "change").click()
        r = reader()
        r.feed(self.driver.page_source)
        data = r.getData()
        processedData = []
        for row in data:
            if len(row) > 0:
                if (row[1] == "Symbol " or row[1] == "CARZ") or row[5] == "-":
                    continue
                processedData.append([row[1],row[2],float(row[5][0:len(row[5])-1])])
        r.clear()
        return processedData

    def getHistoricData(self, symbol: str):
        self.driver.get("https://www.nasdaq.com/market-activity/stocks/"+symbol.lower()+"/historical")
        r = reader()
        r.feed(self.driver.page_source)
        data = r.getData()
        processedData = []
        count = 0
        for row in data:
            if len(row) > 0:
                if row[0] == "Date":
                    continue
                processedData.append([row[0], float(row[1][1:])])
                count+=1
            if count==7:
                break
        r.clear()
        return processedData

    def closeStream(self):
        self.driver.quit()
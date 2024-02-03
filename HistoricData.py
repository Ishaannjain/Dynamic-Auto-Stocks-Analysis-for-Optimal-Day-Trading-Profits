from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from reader import reader
from tabulate import tabulate
import time

options = Options()
# options.add_argument("--headless")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--ssl-errors")
driver = webdriver.Chrome(options=options)
driver.get("https://www.nasdaq.com/market-activity/stocks/meta/historical")
# driver.find_element(By.ID, "change").click()
reader = reader()
reader.feed(driver.page_source)
data = reader.getData()
print(tabulate(data))
# processedData = []
# for row in data:
#     if len(row) > 0:
#         if row[1] == "CARZ" or row[5] == "-":
#             continue
#         processedData.append([row[1],row[5]])
# print(tabulate(processedData))
# time.sleep(5)
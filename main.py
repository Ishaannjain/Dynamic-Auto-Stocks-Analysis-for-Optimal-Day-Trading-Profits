# from DataRetrieval import Driver
# from tabulate import tabulate
# driver = Driver()
# driver.setUp()
# print(tabulate(driver.getTop()))
# print(tabulate(driver.getHistoricData("TSLA")))
from pyweb import pydom
def changeStuff(event):
    pydom["h1#testheader"].html="Data2"
    print("Hello")
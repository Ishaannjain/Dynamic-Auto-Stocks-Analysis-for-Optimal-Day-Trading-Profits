from DataRetrieval import Driver
from pyweb import pydom
import json
driver = Driver()
driver.setUp()
topFive = driver.getTop(5)
symbols = []
dates = []
jsonList = []
count = 1
for element in topFive:
    symbol = element[0]
    pydom["td#N"+count].html = symbol
    pydom["td#S"+count].html = element[1]
    pydom["td#Pr"+count].html = element[3]
    pydom["td#Pt"+count].html = element[4]
    symbols.append(symbol)
    value = driver.getHistoricData(symbol, 7)
    prices = []
    for one in value:
        if len(dates)!=7:
            dates.append(one[0])
        prices.append(one[1])
    jsonList.append(dict(name = symbol, data=prices))
with open("./assets/data/dates.json", "w") as outfile:
    outfile.write(json.dumps(dates))
with open("./assets/data/topFive.json", "w") as outfile:
    outfile.write(json.dumps(symbols))
with open("./assets/data/chartData.json", "w") as outfile:
    outfile.write(json.dumps(jsonList))
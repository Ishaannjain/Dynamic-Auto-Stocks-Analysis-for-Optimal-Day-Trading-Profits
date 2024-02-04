from DataRetrieval import Driver
from tabulate import tabulate
import json, time
driver = Driver()
driver.setUp()
a = time.perf_counter()
topFive = driver.getTop(5)
symbols = []
dates = []
jsonList = []
for element in topFive:
    symbol = element[0]
    symbols.append(symbol)
    value = driver.getHistoricData(symbol, 7)
    prices = []
    for one in value:
        if len(dates)!=7:
            dates.append(one[0])
        prices.append(one[1])
    jsonList.append(dict(name = symbol, data=prices))
    print(time.perf_counter()-a)
with open("./assets/data/dates.json", "w") as outfile:
    outfile.write(json.dumps(dates))
with open("./assets/data/topFive.json", "w") as outfile:
    outfile.write(json.dumps(symbols))
with open("./assets/data/chartData.json", "w") as outfile:
    outfile.write(json.dumps(jsonList))
from html.parser import HTMLParser

class reader(HTMLParser):
    hasData = False
    relevance = False
    Table = list()
    row = list()
    
    def handle_starttag(self, tag, attrs):
        match tag:
            case "table":
                self.hasData = True
            case "tr":
                self.row = list()
            case "td":
                self.relevance = True
            case "th":
                self.relevance = True
    def handle_endtag(self, tag):
        match tag:
            case "tr":
                self.Table.append(self.row)
            case "td":
                self.relevance = False
            case "th":
                self.relevance = False
    def handle_data(self, data):
        if self.relevance == True:
            self.row.append(data)
    def getRow(self):
        return self.row
    def getData(self):
        return self.Table
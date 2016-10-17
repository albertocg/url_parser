import sys
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

links = []
datas = []
word = ""

class URLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(url, value)
                    links.append(newUrl)

    def handle_data(self, data):
        if data.find(word) > -1 and word != "":
            datas.append(data)
    
if __name__ == "__main__":
    if(len(sys.argv) > 1):
        url = sys.argv[1]
        if(len(sys.argv) > 2):
            word = sys.argv[2]

    uParser = URLParser()

    uParser.feed(urlopen(url).read().decode('utf-8'))
    uParser.close()

    for link in links:
        print(link)

    print(len(datas))


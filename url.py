from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

links = []
datas = []

class URLParser(HTMLParser):
    word = ""
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(url, value)
                    links.append(newUrl)

    def handle_data(self, data):
        if data.find(word) > -1:
            datas.append(data)
    
if __name__ == "__main__":
    uParser = URLParser()

    print("Ingrese la URL: ")
    url = input()
    print("Ingrese la palabra a buscar: ")
    uParser.word = input()


    uParser.feed(urlopen(url).read().decode('utf-8'))
    uParser.close()

    for link in links:
        print(link)

    print(len(datas))


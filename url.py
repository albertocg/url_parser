from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

links = []

class URLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(url, value)
                    links.append(newUrl)
    
if __name__ == "__main__":
    uParser = URLParser()

    print("Ingrese la URL: ")
    url = input()


    uParser.feed(urlopen(url).read().decode('utf-8'))
    uParser.close()

    for link in links:
        print(link)


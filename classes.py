import urllib
from bs4 import BeautifulSoup


class TV_parser:
    def __init__(self, url):
        self.resource = urllib.urlopen(url)
        self.source_code = self.resource.readlines()
        self.source_code = [e.rstrip() for e in self.source_code]
        self.source_code = ''.join(self.source_code)
        self.soup = BeautifulSoup(self.source_code)


    def parse(self):



if __name__ == '__main__':
    tv_url = 'http://www.nhl.com/scores/htmlreports/20142015/TV030182.HTM'
    tv_class = TV_parser(tv_url)
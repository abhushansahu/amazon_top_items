from urllib.request import urlopen

from lxml import etree

from utils.helper import return_items_in_bestseller, elements


class ProcessRawfile:
    def __init__(self, **kwargs):
        if 'filename' not in kwargs:
            raise Exception
        self.filename = kwargs.get('filename')
        self.__index = 0
        self.__total_elements = 1
        # self.elements = {
        #     'rank': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/div/span[1]/span',
        #     # 'image': '//*[@id="zg-ordered-list"]/li[{index}}]/span/div/span/a/span/div/img',
        #     'overall_rating': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/span/div[1]/a[1]/i/span',
        #     'name': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/span/a/div',
        #     'price': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/span/div[2]/a/span/span',
        # }

    def __repr__(self):
        return f'Processing file {self.filename}'

    def _loadfile(self):
        response = urlopen(self.filename)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        self.total_elements = len(tree.xpath('//*[@id="zg-ordered-list"]/*'))
        return tree

    @property
    def total_elements(self):
        return self.__total_elements

    @total_elements.setter
    def total_elements(self, n=1):
        self.__total_elements = n

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, n):
        if self.total_elements > n > 0:
            self.__index = n
        else:
            raise IndexError

    def next_index(self):
        try:
            self.index += 1
            while True:
                yield self.index
                self.index += 1
        except IndexError:
            pass

    def parse_element(self):
        tree = self._loadfile()
        elem = {}
        for i in self.next_index():
            for k, v in elements.items():
                val = tree.xpath(v.format(index=i))
                if len(val):
                    elem[k] = tree.xpath(v.format(index=i))[0].text
                    # print(k, tree.xpath(v.format(index=i))[0].text)
            yield elem
        # print('done')


if __name__ == "__main__":
    for i in return_items_in_bestseller('electronics'):
        if i.is_file():
            if str(i).endswith('.html'):
                ProcessRawfile(filename=i.as_uri())

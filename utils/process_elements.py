import re

from utils.helper import return_items_in_bestseller, country_of_origin
from utils.process_raw_file import ProcessRawfile


class ProcessElements:
    def __init__(self, **kwargs):
        self.rank = kwargs.get("rank", 999)
        self.image = kwargs.get("image", None)
        self.overall_rating = kwargs.get("overall_rating", -1)
        self.name = kwargs.get("name", "unknown")
        self.reviewed_by = kwargs.get("reviewed_by", 0)
        self.brand = None
        self.coo = None
        self.price = kwargs.get("price", 0)
        self.process()

    def __repr__(self):
        return f'{self.rank} - {self.brand} - {self.price} - {self.reviewed_by} - {self.coo} - {self.overall_rating}' \
               f' - {self.name}'

    def process(self):
        if type(self.rank) == str:
            self.rank = re.sub('#', '', self.rank)
        if type(self.overall_rating) == str:
            self.overall_rating = float(re.findall('[0-9]{1}.[0-9]{1}', self.overall_rating)[0])
        if self.brand is None:
            self.brand = self.name.split(' ')[0]
        if type(self.price) == str:
            self.price = float(self.price.split('â¹ ')[1].replace(',', ''))
        if self.coo is None:
            self.coo = country_of_origin.get(self.brand.lower(), 'unknown')
        if type(self.reviewed_by) == str:
            self.reviewed_by = int(self.reviewed_by.replace(',', ''))


if __name__ == "__main__":
    for i in return_items_in_bestseller('electronics'):  # smartphones
        if i.is_file():
            if str(i).endswith('.html'):
                for i in ProcessRawfile(filename=i.as_uri()).parse_element():
                    temp = ProcessElements(**i)
                    if temp.coo == 'unknown':
                        print(temp)

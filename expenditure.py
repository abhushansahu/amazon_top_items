import locale
from collections import defaultdict

from utils.helper import return_items_in_bestseller
from utils.process_elements import ProcessElements
from utils.process_raw_file import ProcessRawfile


def printer(teams_list, header):
    print('-----------------------------------------')
    row_format = "|{:>15} | " * (len(teams_list[0]))
    print(row_format.format(*header))
    print('-----------------------------------------')
    for team, row in teams_list:
        print(row_format.format(team, row))
    print('----------------------------------------')


def spent(placeholder_dict):
    a = sorted(placeholder_dict.items(), key=lambda item: item[1], reverse=True)
    b = 0
    while b < len(a):
        a[b] = (a[b][0], locale.currency(a[b][1], grouping=True))
        b += 1
    return a


class Spent(object):
    __instance = {}
    __create_key = object()

    @classmethod
    def get_instance(cls, key):
        if key not in Spent.__instance:
            Spent.__instance[key] = Spent(cls.__create_key)
        return Spent.__instance[key]

    def __init__(self, create_key):
        assert (create_key == Spent.__create_key), "Spent objects must be created using Spent.get_instance(key)"
        self.country_spent = defaultdict(float)
        self.company_spent = defaultdict(float)


class Expenditure:
    def __init__(self, val, key):
        Spent.get_instance(key).country_spent[val.coo] += val.price * val.reviewed_by
        Spent.get_instance(key).company_spent[val.brand] += val.price * val.reviewed_by


if __name__ == "__main__":
    categories = ['smartphones']  # smartphones, electronics
    for c in categories:
        for i in return_items_in_bestseller(c):  # smartphones, electronics
            if i.is_file():
                if str(i).endswith('.html'):
                    for _ in ProcessRawfile(filename=i.as_uri()).parse_element():
                        temp = ProcessElements(**_)
                        Expenditure(temp, c)

        locale.setlocale(locale.LC_MONETARY, 'en_IN')
        print(f'{c} revenue through Amazon.in')
        o = Spent.get_instance(c)
        printer(spent(o.country_spent), ['Country', 'Total Revenue through Amazon.in'])
        printer(spent(o.company_spent), ['Company', 'Total Revenue through Amazon.in'])
        print('')

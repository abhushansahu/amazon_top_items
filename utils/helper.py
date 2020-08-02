from pathlib import Path


def return_items_in_bestseller(key):
    if key.lower() in ('electronics', 'smartphones'):
        path = Path(__file__).parent.parent.joinpath('data/raw/amazon/best_seller').joinpath(key)
        return path.iterdir()
    else:
        raise FileNotFoundError


elements = {
    'rank': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/div/span[1]/span',
    # 'image': '//*[@id="zg-ordered-list"]/li[{index}}]/span/div/span/a/span/div/img',
    'overall_rating': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/span/div[1]/a[1]/i/span',
    'name': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/span/a/div',
    'price': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/span/div[2]/a/span/span',
    'reviewed_by': '//*[@id="zg-ordered-list"]/li[{index}]/span/div/span/div[1]/a[2]'
}

country_of_origin = {
    'samsung': 'South Korea',
    'mi': 'China',
    'boat': 'India',
    'redmi': 'China',
    'logitech': 'Switzerland',
    'lenovo': 'China',
    'zebronics': 'India',
    'philips': 'Netherlands',
    'honor': 'China',
    'sandisk': 'United States',
    'sony': 'Japan',
    'hp': 'United States',
    'realme': 'China',
    'duracell': 'United States',
    'oneplus': 'China',
    'oppo': 'China',
    'nokia': 'Finland',
    'jbl': 'United States',  # samsung acquired?
    'infinity': 'South Korea',  # because harman was acquired by Samsung
    'vivo': 'China',
    'apple': 'China',
    'panasonic': 'Japan',
    'tecno': 'China',
    'itel': 'China',
    'ptron': 'India',
    'popio': 'India',
    'tp-link': 'China',
    'boult': 'India',
    'echo': 'United States',  # Amazon
    'noise': 'India'
}

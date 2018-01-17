import bs4


def parse_html_page(response_text):
    return bs4.BeautifulSoup(response_text, 'html.parser')


def parse_avito_results_page_for_prices(soup):
    descriptions = soup.find_all('div', {'class': 'description'})
    prices_wrappers = [
        d.find('div', {'class': 'about'}) for d in descriptions
    ]
    raw_prices = [w.contents[0] for w in prices_wrappers]
    return filter(None, [process_price(p) for p in raw_prices])


def parse_avito_results_page_for_first_photo(soup):
    photo_wrapper = soup.find('a', {'class': 'photo-wrapper'})
    return 'https:%s' % photo_wrapper.find('img')['src']


def process_price(raw_price):
    price = raw_price.strip()[:-4].replace(' ', '')
    return int(price) if price != '' else None

import requests


def fetch_avito_search_results(query):
    return requests.get(
        'https://www.avito.ru/moskva',
        params={'q': query}
    ).text

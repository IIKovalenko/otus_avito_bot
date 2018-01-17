# coding: utf-8
import logging

from request_helpers import fetch_avito_search_results
from parsers import (
    parse_html_page,
    parse_avito_results_page_for_prices,
    parse_avito_results_page_for_first_photo,
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def price_handler(bot, update):
    # убираем /price из начала запроса
    query = ' '.join(update.message.text.split(' ')[1:])

    response_text = fetch_avito_search_results(query)
    soup = parse_html_page(response_text)
    prices = parse_avito_results_page_for_prices(soup)
    avg_price = sum(prices) / len(prices)
    photo_url = parse_avito_results_page_for_first_photo(soup)

    update.message.reply_text(avg_price)
    bot.send_photo(chat_id=update.message.chat_id, photo=photo_url)

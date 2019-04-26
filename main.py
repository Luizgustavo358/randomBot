from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re


def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_url_cat():
    contents = requests.get('http://aws.random.cat/meow').json()
    url = contents['url']
    return url


def get_image_url_dog():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''

    while file_extension not in allowed_extension:
        url = get_url_dog()
        file_extension = re.search("([^.]*)$", url).group(1).lower()

    return url


def get_image_url_cat():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''

    while file_extension not in allowed_extension:
        url = get_url_cat()
        file_extension = re.search("([^.]*)$", url).group(1).lower()

    return url


def dog(bot, update):
    url = get_image_url_dog()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def cat(bot, update):
    url = get_image_url_cat()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater('836737917:AAFedswsnCAo_8dp-ZWY3td83ag6WZiFbHM')
    dp = updater.dispatcher

    # dog
    dp.add_handler(CommandHandler('dog', dog))

    # cat
    dp.add_handler(CommandHandler('cat', cat))

    updater.start_pooling()
    updater.idle()


if __name__ == '__main__':
    main()

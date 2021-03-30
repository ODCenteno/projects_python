from bs4 import BeautifulSoup as bs
import requests
import schedule


def bot_sendtext(bot_message):
    CHATID = "1114711058"
    TOKEN = "1638992220:AAGoc_PH5pbX60K5ckU0nCWI0QyVNN4oH0Q"
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + CHATID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response


def btc_webscraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = bs(url.content, 'html.parser')
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    format_result = result.text
    return format_result


def report():
    btc_price = f'Ahora el precio de BTC es: {btc_webscraping()}'
    bot_sendtext(btc_price)

if __name__ == '__main__':
    # schedule.every().day.at("08:00").do(report)
    # while True:
    #     schedule.run_pending()

    report()
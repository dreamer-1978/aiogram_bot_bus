from bs4 import BeautifulSoup
import requests

URL_GORG = 'https://yandex.ru/maps/213/moscow/stops/stop__9643755/?ll=37.837812%2C55.779605&tab=overview&z=16.56'
URL_MAIL = 'https://yandex.ru/maps/213/moscow/stops/stop__9643717/?ll=37.826318%2C55.775304&tab=overview&z=16.47'
URL_KUP_RIGHT = 'https://yandex.ru/maps/213/moscow/stops/stop__9643971/?ll=37.823798%2C55.775762&tab=overview&z=17.1'
URL_KUP_LEFT = 'https://yandex.ru/maps/213/moscow/stops/stop__9643718/?ll=37.822873%2C55.775322&tab=overview&z=16.61'


class Parser:
    def __init__(self, url):
        self.bus = 'autobus.txt'
        self.url = url
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                          'Version/15.3 Safari/605.1.15 ',
            'accept': '*/*'
        }

    def erase_content(self):
        with open(self.bus, mode='w') as file:
            file.seek(0)


    def open_content(self):
        with open(self.bus, mode='r') as file:
            bus_content = file.read()
            return bus_content

    def save_content(self, data):
        with open('autobus.txt', mode='a') as file:
            for val, key in data.items():
                file.write(f'{val} : {key}' + '\n')

    def get_url(self):
        req = requests.get(self.url, headers=self.headers)
        if req.status_code == 200:
            return req
        else:
            print('BAD REQUEST')

    def get_content(self):
        soup = BeautifulSoup(self.get_url().text, 'lxml')
        cont_bus = soup.find('ul', class_='masstransit-brief-schedule-view__vehicles').find_all('li',
                                                                                                class_='masstransit-vehicle-snippet-view _clickable _type_bus')
        for cont in cont_bus:
            number_bus = cont.find('a', class_='masstransit-vehicle-snippet-view__name').text.strip()
            time_bus = cont.find('span', class_='masstransit-prognoses-view__title-text').text.strip()

            content = {number_bus: time_bus}
            self.save_content(content)


# parser = Parser(URL_MAIL)
# parser.get_content()
# print(parser.open_content())
# parser.erase_content()

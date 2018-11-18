""""Module with class to work with HTTP client"""

import requests


class HttpClient(object):
    """"Class to work with HTTP request for subscriptions API"""

    def get_subscriptions(self):
        url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=2&system_code=2"
        headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
        return requests.get(url, headers=headers)

    def get_subscriptions_not_authorization(self):
        url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=2&system_code=2"
        return requests.get(url)

    def add_subscriptions(self, instrumentId, secName, secType, price):
        url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=1&system_code=2"
        data = {"instrument_id": instrumentId, "sec_name": secName, "sec_type": secType, "price_alert": price}
        headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
        return requests.post(url, json=data, headers=headers)

    def add_subscriptions_not_authorization(self, instrumentId, secName, secType, price):
        url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=1&system_code=2"
        data = {"instrument_id": instrumentId, "sec_name": secName, "sec_type": secType, "price_alert": price}
        return requests.post(url, json=data)

    def delete_subscriptions(self, id):
        headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
        url = 'https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions/{}?request_id=3&system_code=2'.format(
            id)
        return requests.delete(url, headers=headers)

    def delete_subscriptions_not_authorization(self, id):
        url = 'https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions/{}?request_id=3&system_code=2'.format(
            id)
        return requests.delete(url)

    def delete_all_subscriptions(self):
        url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=2&system_code=2"
        headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
        response = requests.get(url, headers=headers)
        size = len(response.json())
        if (size == 0):
            print("\n" + "Subscriptions list is empty")
            return True
        while (size != 0):
            id = response.json()[size - 1]['id']
            print("\n" + str(response.json()[size - 1]['instrument_id']) + " subscription will be deleted")
            url = 'https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions/{}?request_id=3&system_code=2'.format(
                id)
            result = requests.delete(url, headers=headers)
            if (result.status_code == 200):
                print("OK!")
            else:
                print("Error")
            size -= 1
        return True

    def get_subscriptions_count(self):
        url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=2&system_code=2"
        headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        return len(response.json())

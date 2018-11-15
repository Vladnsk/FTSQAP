import requests


class HttpClient(object):

    def get_subscriptions(self):
        url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=2&system_code=2"
        headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
        return requests.get(url, headers=headers)

    # def add_subscriptions(self, instrumentId, secName, secType, price):
    #     url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=1&system_code=2"
    #     data = {"instrument_id": instrumentId, "sec_name": secName, "sec_type": secType, "price_alert": price}
    #     headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
    #     return requests.post(url, json=data, headers=headers)
    #
    # def delete_subscriptions(self, id):
    #     url = "https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions?request_id=2&system_code=2"
    #     headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
    #     response = requests.get(url, headers=headers)
    #     id = response.json()[0]['id']
    #
    #     url = 'https://fintech-trading-qa.tinkoff.ru/v1/md/contacts/v.kulikov/subscriptions/{}?request_id=3&system_code=2'.format(id)
    #     response = requests.delete(url, headers=headers)
    #     return response

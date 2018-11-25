""""Module with class to work with HTTP client"""

import requests


class HttpClient(object):
    """"Class to work with HTTP request for subscriptions API"""

    def __init__(self):
        self.base = "https://fintech-trading-qa.tinkoff.ru/v1/md/"
        self.auth = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}

    def get_subscriptions(self, request_id, system_code, siebel_id):
        url = self.base + "contacts/" + siebel_id + "/subscriptions?" + "request_id=" + str(request_id) \
              + "&system_code=" + str(system_code)
        return requests.get(url, headers=self.auth)

    def get_subscriptions_not_authorization(self, request_id, system_code, siebel_id):
        url = self.base + "contacts/" + siebel_id + "/subscriptions?" + "request_id=" \
              + str(request_id) + "&system_code=" + str(system_code)
        return requests.get(url)

    def add_subscriptions(self, instrumentId, secName, secType, price, request_id, system_code, siebel_id):
        url = self.base + "contacts/" + siebel_id + "/subscriptions?" + "request_id=" + str(request_id) \
              + "&system_code=" + str(system_code)
        data = {"instrument_id": instrumentId, "sec_name": secName, "sec_type": secType, "price_alert": price}
        return requests.post(url, json=data, headers=self.auth)

    def add_subscriptions_not_authorization(self, instrumentId, secName, secType, price, request_id, system_code, siebel_id):
        url = self.base + "contacts/" + siebel_id + "/subscriptions?" + "request_id=" + str(request_id) \
              + "&system_code=" + str(system_code)
        data = {"instrument_id": instrumentId, "sec_name": secName, "sec_type": secType, "price_alert": price}
        return requests.post(url, json=data)

    def delete_subscriptions(self, id, request_id, system_code, siebel_id):
        url = self.base + "contacts/" + siebel_id + "/subscriptions/{}?".format(id) + "request_id=" + str(request_id) \
              + "&system_code=" + str(system_code)
        return requests.delete(url, headers=self.auth)

    def delete_subscriptions_not_authorization(self, id, request_id, system_code, siebel_id):
        url = self.base + "contacts/" + siebel_id + "/subscriptions/{}?".format(id) + "request_id=" + str(request_id) \
              + "&system_code=" + str(system_code)
        return requests.delete(url)

    def delete_all_subscriptions(self, request_id, system_code, siebel_id):
        url = self.base + "contacts/" + siebel_id + "/subscriptions?" + "request_id=" + str(request_id) \
              + "&system_code=" + str(system_code)
        response = requests.get(url, headers=self.auth)
        size = len(response.json())
        if (size == 0):
            print("\n" + "Subscriptions list is empty")
            return True
        while (size != 0):
            id = response.json()[size - 1]['id']
            print("\n" + str(response.json()[size - 1]['instrument_id']) + " subscription will be deleted")
            url = self.base + "contacts/" + siebel_id + "/subscriptions/{}?".format(id) \
                  + "request_id=" + str(request_id) + "&system_code=" + str(system_code)
            result = requests.delete(url, headers=self.auth)
            if (result.status_code == 200):
                print("OK!")
            else:
                print("Error")
            size -= 1
        return True

    def get_subscriptions_count(self, request_id, system_code, siebel_id):
        url = self.base + "contacts/" + siebel_id + "/subscriptions?" + "request_id=" + str(request_id) \
              + "&system_code=" + str(system_code)
        response = requests.get(url, headers=self.auth)
        assert response.status_code == 200
        return len(response.json())

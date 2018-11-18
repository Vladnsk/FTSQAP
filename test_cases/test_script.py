""""Module with tests to check Investment API - Subscriptions"""

import time
from plugin.plugin import http_client


def test_get_not_authorization(http_client):
    """
    1. Send request to get subscriptions without token
    2. Check response status code is 401
    """
    response = http_client.get_subscriptions_not_authorization()
    assert 401 == response.status_code


def test_add_not_authorization(http_client):
    """
        1. Send request to add subscriptions without token
        2. Check response status code is 401
        3. Check not change count subscriptions
    """
    size = http_client.get_subscriptions_count()
    response = http_client.add_subscriptions_not_authorization("TCS_SPBXM", "TCS", "equity", 20)
    assert 401 == response.status_code
    assert size == http_client.get_subscriptions_count()


def test_delete_not_authorization(http_client):
    """
        1. Send request to add subscriptions without token
        2. Check response status code is 401
        3. Check not change count subscriptions
    """
    http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20)
    size = http_client.get_subscriptions_count()
    id = http_client.get_subscriptions().json()[0]['id']
    response = http_client.delete_subscriptions_not_authorization(id)
    assert 401 == response.status_code
    assert size == http_client.get_subscriptions_count()


def test_get(http_client):
    http_client.delete_all_subscriptions()
    http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20)

    response = http_client.get_subscriptions()
    assert 200 == response.status_code
    assert 1 == len(response.json())

    http_client.delete_all_subscriptions()


def test_add(http_client):
    size = http_client.get_subscriptions_count()
    response = http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20)
    assert 201 == response.status_code
    response = http_client.add_subscriptions("LKOH_TQBR", "LKOH", "equity", 1000)
    assert 201 == response.status_code
    assert size + 2 == http_client.get_subscriptions_count()

    http_client.delete_all_subscriptions()


def test_delete(http_client):
    http_client.delete_all_subscriptions()
    size = http_client.get_subscriptions_count()
    http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20)
    expected = size + 1
    assert expected == http_client.get_subscriptions_count()

    id = http_client.get_subscriptions().json()[0]['id']
    response = http_client.delete_subscriptions(id)
    assert 200 == response.status_code
    assert size == http_client.get_subscriptions_count()


def test_add_bad_argument(http_client):
    size = http_client.get_subscriptions_count()
    response = http_client.add_subscriptions("QWERTY", "TCS", "equity", 20)
    assert 400 == response.status_code
    assert http_client.get_subscriptions_count() == size


def test_add_double_subscriptions(http_client):
    size = http_client.get_subscriptions_count()
    http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20)
    assert size + 1 == http_client.get_subscriptions_count()
    size = size + 1

    response = http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20)
    assert 409 == response.status_code
    assert size == http_client.get_subscriptions_count()

    http_client.delete_all_subscriptions()


def test_double_delete(http_client):
    response = http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20)
    assert 200 == response.status_code

    id = http_client.get_subscriptions().json()[0]['id']
    response = http_client.delete_subscriptions(id)
    assert 200 == response.status_code
    time.sleep(10)
    response = http_client.delete_subscriptions(id)
    assert 404 == response.status_code

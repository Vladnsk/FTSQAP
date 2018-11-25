""""Module with tests to check Investment API - Subscriptions"""

import time
from plugin.plugin import http_client


def test_get_not_authorization(http_client):
    """
    1. Send request to get subscriptions without token
    2. Check response status code is 401
    """
    response = http_client.get_subscriptions_not_authorization(1, 1, "v.kulikov")
    assert 401 == response.status_code


def test_add_not_authorization(http_client):
    """
        1. Send request to add subscriptions without token
        2. Check response status code is 401
        3. Check not change count subscriptions
    """
    size = http_client.get_subscriptions_count(1, 1, "v.kulikov")
    response = http_client.add_subscriptions_not_authorization("TCS_SPBXM", "TCS", "equity", 20, 1, 2, "v.kulikov")
    assert 401 == response.status_code
    assert size == http_client.get_subscriptions_count(1, 1, "v.kulikov")


def test_delete_not_authorization(http_client):
    """
        1. Send request to add subscriptions without token
        2. Check response status code is 401
        3. Check not change count subscriptions
    """
    http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20, 1, 1, "v.kulikov")
    size = http_client.get_subscriptions_count(1, 1, "v.kulikov")
    id = http_client.get_subscriptions(1, 1, "v.kulikov").json()[0]['id']
    response = http_client.delete_subscriptions_not_authorization(id, 1, 1, "v.kulikov")
    assert 401 == response.status_code
    assert size == http_client.get_subscriptions_count(1, 1, "v.kulikov")


def test_get(http_client):
    http_client.delete_all_subscriptions(1, 1, "v.kulikov")
    http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20, 1, 1, "v.kulikov")

    response = http_client.get_subscriptions(1, 1, "v.kulikov")
    assert 200 == response.status_code
    assert 1 == len(response.json())

    http_client.delete_all_subscriptions(1, 1, "v.kulikov")


def test_add(http_client):
    size = http_client.get_subscriptions_count(1, 1, "v.kulikov")
    response = http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20, 1, 1, "v.kulikov")
    assert 201 == response.status_code
    response = http_client.add_subscriptions("LKOH_TQBR", "LKOH", "equity", 1000, 1, 1, "v.kulikov")
    assert 201 == response.status_code
    assert size + 2 == http_client.get_subscriptions_count(1, 1, "v.kulikov")

    http_client.delete_all_subscriptions(1, 1, "v.kulikov")


def test_delete(http_client):
    http_client.delete_all_subscriptions(1, 1, "v.kulikov")
    size = http_client.get_subscriptions_count(1, 1, "v.kulikov")
    http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20, 1, 1, "v.kulikov")
    expected = size + 1
    assert expected == http_client.get_subscriptions_count(1, 1, "v.kulikov")

    id = http_client.get_subscriptions(1, 1, "v.kulikov").json()[0]['id']
    response = http_client.delete_subscriptions(id, 1, 1, "v.kulikov")
    assert 200 == response.status_code
    assert size == http_client.get_subscriptions_count(1, 1, "v.kulikov")


def test_add_bad_argument(http_client):
    size = http_client.get_subscriptions_count(1, 1, "v.kulikov")
    response = http_client.add_subscriptions("QWERTY", "TCS", "equity", 20, 1, 1, "v.kulikov")
    assert 400 == response.status_code
    assert http_client.get_subscriptions_count(1, 1, "v.kulikov") == size


def test_add_double_subscriptions(http_client):
    size = http_client.get_subscriptions_count(1, 1, "v.kulikov")
    http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20, 1, 1, "v.kulikov")
    assert size + 1 == http_client.get_subscriptions_count(1, 1, "v.kulikov")
    size = size + 1

    response = http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20, 1, 1, "v.kulikov")
    assert 409 == response.status_code
    assert size == http_client.get_subscriptions_count(1, 1, "v.kulikov")

    http_client.delete_all_subscriptions(1, 1, "v.kulikov")


def test_double_delete(http_client):
    response = http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20, 1, 1, "v.kulikov")
    assert 200 == response.status_code

    id = http_client.get_subscriptions(1, 1, "v.kulikov").json()[0]['id']
    response = http_client.delete_subscriptions(id, 1, 1, "v.kulikov")
    assert 200 == response.status_code
    time.sleep(10)
    response = http_client.delete_subscriptions(id, 1, 1, "v.kulikov")
    assert 404 == response.status_code

def test_add(http_client):
    response = http_client.add_subscriptions("TCS_SPBXM", "TCS", "equity", 20)
    assert response.status_code == 200
    print(response.content)


def test_get(http_client):
    response = http_client.get_subscriptions()
    assert response.status_code == 200
    print(response.content)


def test_delete(http_client):
    id = http_client.get_subscriptions().json()[0]['id']
    response = http_client.delete_subscriptions(id)
    assert response.status_code == 200
    print(response.content)


def test_get2(http_client):
    response = http_client.get_subscriptions()
    assert response.status_code == 200
    print(response.content)

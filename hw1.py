import requests as req

url = "https://api.github.com"
userName = "Vladnsk"
myToken = ""
authHead = {'Authorization': 'token {}'.format(myToken)}


def test_get_github_account(user):
    response = req.get(url + "/users/" + user)

    assert response.status_code == 200
    assert len(response.content) > 0

    print(response.content)


def test_get_github_repos():
    response = req.get(url + "/user/repos", headers=authHead)

    assert response.status_code == 200
    assert len(response.content) > 0

    print(response.content)


if len(myToken) == 0:
    print("Incorrect token")
    print("Test 1/2:")
    test_get_github_account(userName)
else:
    print("Test 1/2:")
    test_get_github_account(userName)
    print("Test 2/2:")
    test_get_github_repos()

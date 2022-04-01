def test_count_words_returns_expected_occurrences(client):
    response = client.get("/count-words?url=https://www.bbc.co.uk")
    assert response.status_code == 200
    assert response.data != {}


def test_count_words_returns_404_if_url_is_not_provided(client):
    response = client.get("/count-words")
    assert response.status_code == 400
    assert b"error" in response.data
    assert b"Url must be provided" in response.data


def test_count_words_returns_404_if_url_does_not_exist(client):
    response = client.get("/count-words?url=http://www.invaliddomainname.com")
    assert response.status_code == 404
    assert b"error" in response.data
    assert b"http://www.invaliddomainname.com does not exist" in response.data


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert b"status" in response.data
    assert b"UP" in response.data
    assert b"message" in response.data

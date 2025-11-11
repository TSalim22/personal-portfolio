from app import create_app, PROJECTS


def test_portfolio_links_and_semantics():
    client = create_app().test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'lang="en"' in response.data
    for _, repository, _, _ in PROJECTS:
        link = f'https://github.com/TSalim22/{repository}'.encode()
        assert link in response.data
    assert b'GitHub upload pending' not in response.data
    assert client.get('/robots.txt').status_code == 200

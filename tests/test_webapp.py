from webapp.app import create_app


def test_index_and_health():
    client = create_app().test_client()
    assert client.get("/").status_code == 200
    assert client.get("/healthz").json == {"status": "ok"}

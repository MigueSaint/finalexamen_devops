import app

def test_status_endpoint():
    client = app.app.test_client()
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json["status"] == "ok"

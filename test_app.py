import app

def test_status_endpoint():
    client = app.app.test_client()
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_home_get():
    client = app.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Bienvenido" in response.data  # Busca texto en HTML


def test_home_post_name():
    client = app.app.test_client()
    response = client.post("/", data={"nombre": "Miguel"})

    assert response.status_code == 200
    assert b"Miguel" in response.data  # Verifica saludo dinámico


def test_json_endpoint():
    client = app.app.test_client()
    response = client.get("/api/info")

    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert "app" in response.json


def test_not_found():
    client = app.app.test_client()
    response = client.get("/ruta-que-no-existe")

    assert response.status_code == 404

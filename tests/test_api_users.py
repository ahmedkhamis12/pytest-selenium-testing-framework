from framework.utils import validate_status

def test_get_users(api):
    response = api.get_users()
    validate_status(response, 200)
    assert "data" in response.json()

def test_create_user(api):
    payload = {"name": "Ahmed", "job": "QA Engineer"}
    response = api.create_user(payload)
    validate_status(response, 201)
    assert response.json()["name"] == "Ahmed"

def test_update_user(api):
    payload = {"name": "Updated", "job": "Tester"}
    response = api.update_user(2, payload)
    validate_status(response, 200)

def test_delete_user(api):
    response = api.delete_user(2)
    validate_status(response, 204)

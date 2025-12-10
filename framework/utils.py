def validate_status(response, expected=200):
    assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"

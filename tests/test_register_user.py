import pytest
import requests
from utils.auth_helpers import AuthActions

def test_register_user():
    auth = AuthActions()
    response = auth.register_user()
    print(response)
    assert response.status_code == 201

def test_register_already_registered_user():
    auth = AuthActions()
    response = auth.register_user()
    print(response)
    assert response.status_code == 400






import pytest
import requests
import json
from utils.auth_helpers import AuthActions

def test_resend_otp():
    auth = AuthActions()
    response = auth.resend_otp()
    responsebody = response.json()
    print(responsebody)
    assert response.status_code == 201

def test_resend_otp_with_unregistered_user():
    auth = AuthActions()
    response = auth.resend_otp()
    responsebody = response.json()
    assert response.status_code == 400







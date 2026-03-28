import pytest
from client import APIClient
@pytest.fixture
def client():
    return APIClient()

    
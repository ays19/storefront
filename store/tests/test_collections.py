from rest_framework import status
from rest_framework.test import APIClient
import pytest

    
@pytest.mark.django_db
class TestCreateCollection:
    #@pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self):
        #tests should have 3parts AAA
        #Arrange(this test has no arrange)

        #ACT
        client = APIClient()
        response = client.post('/store/collections/', { 'title': 'a' })

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
from rest_framework.test import APITestCase
import pytest
from contacts.models import Contact

class Test_test(APITestCase):
    def Test_create(self):
        assert 1 == 1
        data = {'name': 'Lino', 'telephone': '940596713', 'ddd': '11'}
        response = self.client.post("api/create/", data)



@pytest.fixture()
def test_user_1(db):
    data = {'name': 'Lino', 'telephone': '940596713', 'ddd': '11'}
    return Contact.objects.create_user(data)
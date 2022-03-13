from turtle import pd
from django.test import TestCase
from rest_framework.test import APIClient
import pdb
import json


class TestMovieView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.contat_data = {"name": "Lino", "telephone": "940596713", "ddd":"11"}
        self.contat_data_1 = {"name": "Leandro", "telephone": "940596713", "ddd":"11"}
        self.contat_data_put = {"name": "Leandro", "telephone": "940596713", "ddd":"11"}
        self.contat_data_put_conflit = {"name": "Leandro", "telephone": "940596714", "ddd":"11"}

    def test_create_contact(self):
        # create contact
        created = self.client.post("/api/create/", self.contat_data, format="json")

        self.assertEqual(created.json()["id"], 1)
        self.assertEqual(created.status_code, 201)

        listed = self.client.get("/api/list/", format="json")
        self.assertEqual(len(listed.json()), 1)

    def test_create_contact_with_conflit(self):
        # create contact
        created = self.client.post("/api/create/", self.contat_data, format="json")

        self.assertEqual(created.json()["id"], 1)
        self.assertEqual(created.status_code, 201)

        created = self.client.post("/api/create/", self.contat_data_1, format="json")
        self.assertEqual(created.json(), {'Error': 'This telephone already exist'})
        self.assertEqual(created.status_code, 409)

        listed = self.client.get("/api/list/", self.contat_data, format="json")
        self.assertEqual(len(listed.json()), 1)

    def test_update_contact(self):
        # create contact
        created = self.client.post("/api/create/", self.contat_data, format="json")
        self.assertEqual(created.json()["id"], 1)
        self.assertEqual(created.status_code, 201)

        created = self.client.put("/api/edit/1/", self.contat_data_put, format="json")
        self.assertEqual(created.json()["name"], "Leandro" )
        self.assertEqual(created.status_code, 202)

    def test_update_contact_with_conflit(self):
        # create contact
        created = self.client.post("/api/create/", self.contat_data_put, format="json")
        self.assertEqual(created.json()["id"], 1)
        self.assertEqual(created.status_code, 201)
        created = self.client.post("/api/create/", self.contat_data_put_conflit, format="json")
        self.assertEqual(created.json()["id"], 2)
        self.assertEqual(created.status_code, 201)

        created = self.client.put("/api/edit/2/", self.contat_data_put, format="json")
        self.assertEqual(created.json(), {"Error": "This telephone already exist"} )
        self.assertEqual(created.status_code, 409)



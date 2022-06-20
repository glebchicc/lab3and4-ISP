from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.


class TestClass(TestCase):
    def setUP(self):
        self.login_url = '/login/'
        user = User.objects.create(username='programtest')
        user.set_password('123456')
        user.save()
        self.client.login(username='programtest', password='123456')

    def test_registration(self):
        data = {'username': 'regTestUser', 'password': '147258', 'password2': '147258'}
        response = self.client.post("/register/", data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        data = {'username': 'regTestUser', 'password': '147258', 'password2': '147258'}
        self.client.post("/register/", data=data, follow=True)
        response = self.client.post("/login/", data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_addBus_notAdmin(self):
        data = {'bus_number': '100', 'departure_time': '21.06.2022 17:56:21', 'arrival_time': '21.06.2022 19:26:21', 'departure_place': 'Зазеркалье', 'arrival_place': 'Изумрудный город', 'place_cost': '5.0', 'places': '17', 'size_of_bus_id': 2}
        self.client.login(username='programtest', password='123456')
        response = self.client.post('/crud/', data=data)
        self.assertEqual(response.status_code, 404)

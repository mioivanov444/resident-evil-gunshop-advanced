from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from guns.models import Gun, Category
from rest_framework.test import APITestCase


class GunModelTests(TestCase):

    def test_create_gun(self):
        self.gun = Gun.objects.create(name="AK-47", stock=10)
        self.assertEqual(self.gun.stock, 10)

    def test_gun_str(self):
        self.gun = Gun.objects.create(name="Desert Eagle", stock=5)
        self.assertEqual(str(self.gun), self.gun.name)

    def test_default_stock(self):
        self.gun = Gun.objects.create(name="Pistol")
        self.assertEqual(self.gun.stock, 0)

    def test_category_relationship(self):
        self.gun = Gun.objects.create(name="Shotgun", stock=3)
        category = Category.objects.create(name="Heavy")
        self.gun.categories.add(category)
        self.assertIn(category, self.gun.categories.all())

    def test_multiple_categories(self):
        self.gun = Gun.objects.create(name="SMG", stock=7)
        c1 = Category.objects.create(name="Auto")
        c2 = Category.objects.create(name="Fast")
        self.gun.categories.add(c1, c2)
        self.assertEqual(self.gun.categories.count(), 2)



class AuthTests(TestCase):

    def test_user_registration(self):
        user = User.objects.create_user(username="testuser", password="1234")
        self.assertEqual(user.username, "testuser")

    def test_user_login(self):
        User.objects.create_user(username="testuser", password="1234")
        login = self.client.login(username="testuser", password="1234")
        self.assertTrue(login)

    def test_user_logout(self):
        User.objects.create_user(username="testuser", password="1234")
        self.client.login(username="testuser", password="1234")
        response = self.client.post("/users/logout/")
        self.assertIn(response.status_code, [200, 302])

    def test_authenticated_access(self):
        User.objects.create_user(username="testuser", password="1234")
        self.client.login(username="testuser", password="1234")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_anonymous_access(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class ViewTests(APITestCase):

    def setUp(self):
        self.gun = Gun.objects.create(name="AK-47", stock=10)

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_gun_list_api(self):
        url = reverse('api_gun_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('AK-47', str(response.content))

    def test_gun_detail_api(self):
        url = reverse('api_gun_detail', kwargs={'slug': self.gun.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.gun.name, str(response.content))

    def test_send_email_api(self):
        url = reverse('send_email')
        data = {"email": "test@example.com"}
        response = self.client.post(url, data, format='json')
        self.assertIn(response.status_code, [200, 201, 202])
        self.assertIn('task_id', response.data)

    def test_404_page(self):
        response = self.client.get("/non-existent-page/")
        self.assertEqual(response.status_code, 404)

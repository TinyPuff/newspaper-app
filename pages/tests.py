from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

class HomePageTests(TestCase):


    def test_home_page_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home Page")
        self.assertTemplateUsed(response, "home.html")
    


class SignUpPageTests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@testmail.com",
            age="20",
            password="testpass",
        )
    
    def test_sign_up_page_exists(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_sign_up_page_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
    
    def test_sign_up_form(self):
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "test@testmail.com")
        self.assertEqual(str(get_user_model().objects.all()[0].age), "20")
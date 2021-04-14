from django.test import TestCase
from django.urls import reverse
from django.urls import resolve

# Create your tests here.

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 200)

    
    def test_home_url_resolves_home_view(self):
        # Resolve function to match requested
        # URLs with a list of URLs, in the urls.py module
        view = resolve('/')
        self.assertEquals(view.func, home)

from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home, board_topics
from .models import Board

# Create your tests here.

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.responce = self.client.get(url)


    def test_home_view_status_code(self):
        self.assertEquals(self.responce.status_code, 200)

    
    def test_home_url_resolves_home_view(self):
        # Resolve function to match requested
        # URLs with a list of URLs, in the urls.py module
        view = resolve('/')
        self.assertEquals(view.func, home)

    #The new test here is the test_home_view_contains_link_to_topics_page. Here we are using the assertContains method to test if 
    #the response body contains a given text. The text we are using in the test, is the href part of an a tag. 
    #So basically we are testing if the response body has the text href="/boards/1/".
    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.responce, 'href="{0}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", description="Djangp board.")


    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 200)

    
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 404)

    
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)


        
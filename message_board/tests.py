from django.test import TestCase
from django.urls import reverse
from .models import post

# Create your tests here.

class PostTests (TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = post.objects.create(text = "from test.py")
        
    def test_model_content(self):
        self.assertEqual(self.post.text, "from test.py")
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_message_board(self):
        response = self.client.get(reverse("message_board"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "message_board/post.html")
        self.assertContains(response, '<h1 class="app-name">Message Board</h1>')

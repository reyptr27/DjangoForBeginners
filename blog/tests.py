from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import post

# Create your tests here.

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testuser", 
            email = "test@gmail.com", 
            password = "rahasia",
        )
        
        cls.post = post.objects.create(
            title = "Test Blog App",
            author = cls.user,
            content = "coba blog app",
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.title, "Test Blog App")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.content, "coba blog app")
        self.assertEqual(str(self.post), "Test Blog App")  
        self.assertEqual(self.post.get_absolute_url(), "/blog/1/")
    
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)
    
    def test_blog_listview(self):
        response = self.client.get(reverse("blogpage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog.html")
        self.assertContains(response, '<h1 class="app-name">Blog App</h1>')
    
    def test_blog_detailview(self):
        response = self.client.get(reverse("blogpage_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get( "/blog/100/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "blog/blog_detail.html")
        self.assertContains(response, '<h1 class="app-name">Blog App Post Detail</h1>')
        self.assertContains(response, 'Test Blog App')
        self.assertContains(response, 'testuser')
            
    
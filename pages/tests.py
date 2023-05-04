from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "pages/home.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, '<h1 class="app-name">ini Homepage</h1>')
    

class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("aboutpage"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("aboutpage"))
        self.assertTemplateUsed(response, "pages/about.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("aboutpage"))
        self.assertContains(response, '<h1 class="app-name">ini Aboutpage</h1>')
    
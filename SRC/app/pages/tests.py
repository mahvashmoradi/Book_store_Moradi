from django.test import TestCase

# Create your tests here.
from django.urls import reverse, reverse_lazy


class BookTest(TestCase):

    def test_home(self):
        response = self.client.get(reverse_lazy('pages:home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'pages/home.html')
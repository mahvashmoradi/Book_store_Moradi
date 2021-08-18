from django.test import TestCase
from .models import BookModel, Author


# Create your tests here.

class BookTest(TestCase):
    def setUp(self):
        author = Author.objects.create(name='ali')
        BookModel.objects.create(name='divan', price=100000, author=author)

    def test_check_name(self):
        self.assertEquals(BookModel.objects.last().name, 'divan')



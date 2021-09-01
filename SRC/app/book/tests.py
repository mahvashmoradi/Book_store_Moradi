from django.test import TestCase


# Create your tests here.
from app.book.models import *


class BookTest(TestCase):
    def setUp(self):
        author = Author.objects.create(name='ali')
        BookModel.objects.create(name='divan', price=100000, author=author)

    def test_check_name(self):
        self.assertEquals(BookModel.objects.last().name, 'divan')



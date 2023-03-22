from concertconnect_app.models import Category
from django.test import SimpleTestCase

class ConcertMethodTests(TestCase):
    def test_ensure_views_are_positive(self):

        category = Category(name='Test', views =-1. likes=0)
        concert.save()
        self.assertEqual((category.views>=0), True)

    def test_slug_line_creation(self):
        category = Category(name='Random Category String')
        concert.save()
        self.assertEqual(category.slug, 'random-category-string')
        
    
        

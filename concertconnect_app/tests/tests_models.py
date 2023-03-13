from rangoi.models import concerts
from django.test import SimpleTestCase

class ConcertMethodTests(TestCase):
    def test_ensure_views_are_positive(self):

        concert = Concert(name='Test', views =-1. likes=0)
        concert.save()
        self.assertEqual((concert.views>=0), True)

    def test_slug_line_creation(self):
        concert = Concert(name='Random Concert String')
        concert.save()
        self.assertEqual(concert.slug, 'random-concert-string')
        
    
        

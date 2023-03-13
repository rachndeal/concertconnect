from django.test import SimpleTestCase
from django.urls import reverse, resolve
from concertconnect_app.views import index, concerts

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolves(self):
        url = reverse("index")
        print(resolve(url))
        self.assertEquals(resolved(url).func, index)

    def test_concerts_is_resolved(self):
        url = reverse("concerts")
        print(resolve(url))
        self.assertEquals(resolved(url).func, concert)

  



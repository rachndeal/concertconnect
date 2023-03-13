from django.test import TestCase, Client
from django.urls import reverse


class IndexTestViews(TestCase):
    def test_index_with_no_categories(self):
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present')
        self.assertQuerysetEqual;(response.context['categories'], [])

    def add_category(nsme, views=0, likes=0):
        category = Category.objects.get_or_create(name=name)[0]
        category.views =views
        category.likes = likes
        category.save()
        return category

    def test_index_view_with_categories(self):
        add_category('Python', 1 ,1)
        add_category('C++', 1, 1)
        add_category('Erling', 1, 1)
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertConatins(response, "Python")
        self.assertConatins(response, "C++")
        self.assertConatins(response, "Erling")
        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 3)

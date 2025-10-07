from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        shakshuka = MenuItem.objects.create(dish="shakshuka", price=7, inventory=100)
        burger = MenuItem.objects.create(dish="burger", price=9, inventory=50)

    def test_get_all(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['dish'], 'shakshuka')
        self.assertEqual(response.data[1]['dish'], 'burger')
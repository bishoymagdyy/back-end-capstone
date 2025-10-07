from django.test import TestCase
from restaurant.models import MenuItem

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(dish="IceCream", price=8, inventory=100)
        self.assertEqual(str(item), "IceCream : 8")
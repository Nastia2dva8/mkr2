from django.test import TestCase
from gallery.models import Category, Image
from datetime import date

class CategoryModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Nature")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Nature")
        self.assertEqual(str(self.category), "Nature")

class ImageModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Nature")
        self.image = Image.objects.create(
            title="Sunset",
            image="images/sunset.jpg",  # Фіктивний шлях для тесту
            created_date=date(2025, 5, 23),
            age_limit=18
        )
        self.image.categories.add(self.category)

    def test_image_creation(self):
        self.assertEqual(self.image.title, "Sunset")
        self.assertEqual(self.image.created_date, date(2025, 5, 23))
        self.assertEqual(self.image.age_limit, 18)
        self.assertEqual(str(self.image), "Sunset")

    def test_image_categories(self):
        self.assertEqual(self.image.categories.count(), 1)
        self.assertEqual(self.image.categories.first().name, "Nature")

    def test_image_age_limit_positive(self):
        self.assertGreaterEqual(self.image.age_limit, 0)
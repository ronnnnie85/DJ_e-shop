from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products and categories to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category1, _ = Category.objects.get_or_create(name='Телевизоры Samsung', description='Все телевизоры с разными технологиями')
        category2, _ = Category.objects.get_or_create(name='Телефоны Samsung', description='Все телефоны с разными технологиями')

        products = [
            {'name': 'Samsung TV75', 'description': 'Большой телевизор Samsung', 'category': category1, 'price': 119000.00},
            {'name': 'Samsung TV55', 'description': 'Маленький телевизор Samsung', 'category': category1, 'price': 69000.00},
            {'name': 'Samsung S75', 'description': 'Телефон Samsung с ИИ', 'category': category2, 'price': 119000.00},
            {'name': 'Samsung A75', 'description': 'Самый простой телефон Samsung', 'category': category2, 'price': 49000.00}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name} {product.description}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name} {product.description}'))

        call_command('loaddata', 'catalog_Category_fixture.json')
        call_command('loaddata', 'catalog_Product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
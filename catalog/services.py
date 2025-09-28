from catalog.models import Product


def get_products_category(category_id):
    return Product.objects.filter(category__id=category_id).all()
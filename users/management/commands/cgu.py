from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        moders_group = Group.objects.create(name='Модератор продуктов')
        moders_group.save()

        can_unpublish_product = Permission.objects.get(codename='can_unpublish_product')
        delete_product_permission = Permission.objects.get(codename='delete_product')

        # Назначаем разрешения группе
        moders_group.permissions.add(can_unpublish_product, delete_product_permission)



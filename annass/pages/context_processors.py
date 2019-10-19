from .models import Kontakt
from shop.models import ProductCategory
def kontakt(request):
    return {'kontakt': Kontakt.objects.get(pk=2)}


def version(request):
    return {'version': '1.6'}


def create_main_category_if_not_exists(request):
    if not ProductCategory.objects.filter(name="Alle"):
        all = ProductCategory()
        all.name = "Alle"
        all.save()
    return {}

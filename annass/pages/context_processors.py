from .models import Kontakt
def kontakt(request):
    return {'kontakt': Kontakt.objects.get(pk=1)}


def version(request):
    return {'version': '1.3'}

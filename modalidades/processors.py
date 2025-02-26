from modalidades.models import Modalidad

def ctx_dict(request):
    ctx = {'modalidades': Modalidad.objects.all() }
    return ctx
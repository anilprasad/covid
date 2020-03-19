from source.apps.core.models import MapsArcgisModel


def get_all():
    return MapsArcgisModel.objects.all()

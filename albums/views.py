from rest_framework import viewsets
from .models import Album, Artist, Genre
from .serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('rank')
    serializer_class = AlbumSerializer

    def get_options(self):
        return "options", {
            "artist": [{'label': obj.name, 'value': obj.pk} for obj in Artist.objects.all()],
            "genre": [{'label': obj.name, 'value': obj.pk} for obj in Genre.objects.all()]
        }

    class Meta:
        datatables_extra_json = ('get_options',)
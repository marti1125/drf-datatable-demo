from django.conf.urls import url, include
from rest_framework import routers
from albums import views

router = routers.DefaultRouter()
router.register('albums', views.AlbumViewSet)

urlpatterns = router.urls
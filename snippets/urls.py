"""Urls.py module."""

from django.conf.urls import url, include
from snippets.views import UserViewSet, SnippetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))

]

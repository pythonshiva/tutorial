"""Views module."""

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from snippets.models import Snippet
from snippets.serializers import UserSerializer
from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This view set handles list and details views."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This class handles 'list', 'update', 'retrieve',
       'create', 'destroy' actions.

    And additionally we also provideing extra highlight option
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        """For highlighting the code snippet."""
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def pre_save(self, obj):
        """For sending user name while handling the data."""
        self.owner = self.request.user

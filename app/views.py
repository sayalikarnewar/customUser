from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
#from rest_framework.views import APIView
#from rest_framework.parsers import JSONParser
#from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from app.models import User
from app.serializers import UserSerializer
from app.permissions import IsOwnerOrReadOnly
# Create your views here.



class AppViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        app = self.get_object()
        return Response(app.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

 
 
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AppHighlight(generics.GenericAPIView):
    queryset = User.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        app = self.get_object()
        return Response(app.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'app': reverse('app-list', request=request, format=format),
        'user': reverse('user-list', request=request, format=format),

    })

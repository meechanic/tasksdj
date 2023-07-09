import tasks.serializers as tasks_serializers
import tasks.models as tasks_models
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'tasks': reverse('task', request=request),
        'taskstags': reverse('tasktag', request=request),
    })


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiTask(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = tasks_models.Task.objects.all()
    serializer_class = tasks_serializers.TaskSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name', 'human_description')
    search_fields=('name', 'human_description')


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiTaskTag(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = tasks_models.TaskTag.objects.all()
    serializer_class = tasks_serializers.TaskTagSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('key', 'value')
    search_fields=('key', 'value')

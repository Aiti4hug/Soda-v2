from .serializers import *
from .models import *
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
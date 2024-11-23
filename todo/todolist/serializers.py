from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
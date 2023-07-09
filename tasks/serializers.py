import tasks.models as tasks_models
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks_models.Task
        fields = '__all__'


class TaskTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks_models.TaskTag
        fields = '__all__'

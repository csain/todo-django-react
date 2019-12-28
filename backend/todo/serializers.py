from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    # Specify the model to work with and fields to serialize
    model = Todo
    fields = ('id', 'title', 'description', 'completed')

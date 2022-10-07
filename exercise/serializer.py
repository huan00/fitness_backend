from rest_framework import serializers
from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Exercise
    fields = (
      'id',
      'name',
      'gifUrl',
      'target',
      'bodyParts',
      'equipment'
    )

class NewExerciseSerializer(serializers.ModelSerializer):
  class Meta: model = Exercise
  fields = (
    'name',
    'gifUrl',
    'target',
    'bodyParts',
    'equipment',
  )
  def create(self, validated_data):
    # exercise_data = validated_data()
    return Exercise.objects.create(**validated_data)
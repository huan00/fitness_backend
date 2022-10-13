from rest_framework import serializers
from .models import Session, Workout, ExerciseSet
from exercise.serializers import ExerciseSerializer


class MyExerciseSetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = ExerciseSet
        fields = (
            'set',
            'rep',
            'weight',
            'exercise',
        )


class ExerciseSetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = ExerciseSet
        fields = (
            'exercise',
            'set',
            'rep',
            'weight',

        )


class MyWorkoutSerializer(serializers.ModelSerializer):
    exercise_set = MyExerciseSetSerializer(many=True)

    class Meta:
        model = Workout
        fields = (
            'created_at',
            'exercise_set'
        )


class MySessionSerializer(serializers.ModelSerializer):
    workout = MyWorkoutSerializer(many=True)

    class Meta:
        model = Session
        fields = (
            'created_at',
            'workout_day',
            'focus_area',
            'workout'
        )


class WorkoutSerializer(serializers.ModelSerializer):
    exercise_set = ExerciseSetSerializer(many=True)

    class Meta:
        model = Workout
        fields = (
            'created_at',
            'exercise_set'
        )


class SessionSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer(many=True)

    class Meta:
        model = Session
        fields = (
            'created_at',
            'workout_day',
            'focus_area',
            'workout'
        )

    # def create(self, validated_data):
    #     sets_data = validated_data.pop('workout')
    #     session = Session.objects.create(**validated_data)

    #     for set in sets_data:
    #         WorkoutSet.objects.create(session=session, **set)

    #     return session
